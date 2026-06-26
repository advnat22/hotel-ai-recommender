# rank_hotels.py

import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(

    "processed_hotels.json",

    encoding="utf-8"

) as f:

    hotels=json.load(f)

user_query="""
Looking for a clean hotel
with good food and transport
"""

user_emb=model.encode(

    [user_query]

)

for hotel in hotels:

    hotel_text=f"""
    Hotel: {hotel['name']}

    Food score: {hotel['food']}

    Transport score: {hotel['transport']}

    Luxury score: {hotel['luxury']}

    Cleanliness score: {hotel['cleanliness']}

    Sentiment score: {hotel['sentiment']}
    """

    hotel_emb=model.encode(

        [hotel_text]

    )

    hotel["match_score"]=float(

        cosine_similarity(

            user_emb,

            hotel_emb

        )[0][0]

    )

hotels.sort(

    key=lambda x:x["match_score"],

    reverse=True

)

for hotel in hotels[:10]:

    print(

        hotel["name"],

        hotel["match_score"]

    )