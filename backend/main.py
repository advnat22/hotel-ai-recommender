from fastapi import FastAPI
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from backend import models
from backend import schemas

from backend.database import engine
from backend.database import get_db
from backend.database import Base

from pathlib import Path
import json

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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


@app.get("/search")
def search():

    file_path = Path(__file__).parent / "processed_hotels.json"

    with open(file_path, encoding="utf-8") as f:
        hotels = json.load(f)

    results = []

    for hotel in hotels:
        rating = hotel.get("rating", 0)

        score = round(rating * 2, 1)

        results.append({
            "name": hotel["displayName"]["text"],
            "address": hotel["formattedAddress"],
            "rating": rating,
            "score": score,
            "summary": hotel.get(
                "summary",
                "Summary unavailable"
            )
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:10]