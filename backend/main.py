from fastapi import FastAPI
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import models
import schemas

from database import engine
from database import get_db
from database import Base   

from pathlib import Path
import json

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://hotel-ai-recommender-zgf2.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "backend working"
    }


@app.post("/signup")
def signup(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing:
        return {
            "message": "email already exists"
        }

    new_user = models.User(
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "user_id": new_user.id
    }


@app.post("/login")
def login(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email,
        models.User.password == user.password
    ).first()

    if existing_user:
        return {
            "message": "success",
            "user_id": existing_user.id
        }

    return {
        "message": "invalid"
    }


@app.post("/preferences")
def save_preferences(
    pref: schemas.PreferenceCreate,
    db: Session = Depends(get_db)
):
    new_pref = models.Preference(
        user_id=pref.user_id,
        budget=pref.budget,
        trip_type=pref.trip_type,
        food=pref.food,
        transport=pref.transport,
        luxury=pref.luxury,
        cleanliness=pref.cleanliness
    )

    db.add(new_pref)
    db.commit()

    return {
        "message": "saved"
    }

import ranking_engine

@app.get("/search")
def search(
    user_id: int,
    db: Session = Depends(get_db)
):
    pref = db.query(models.Preference).filter(
        models.Preference.user_id == user_id
    ).order_by(models.Preference.id.desc()).first()

    if not pref:
        return {"message": "No preferences found for this user"}

    pref_dict = {
        "food": pref.food,
        "transport": pref.transport,
        "luxury": pref.luxury,
        "cleanliness": pref.cleanliness
    }

    file_path = Path(__file__).parent / "processed_hotels.json"

    with open(file_path, encoding="utf-8") as f:
        hotels = json.load(f)

    results = []

    for hotel in hotels:
        score = ranking_engine.hotel_score(hotel, pref_dict)

        results.append({
            "name": hotel["name"],
            "address": hotel["address"],
            "rating": hotel.get("rating", 0),
            "score": round(score, 2),
            "summary": hotel.get("summary", "Summary unavailable")
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:10]
