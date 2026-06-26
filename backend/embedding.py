# embeddings.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

user_query = """
Looking for a clean hotel
with good food and transport
"""

hotel_review_text = """
Great breakfast.
MRT nearby.
Very clean rooms.
"""

user_emb = model.encode(
    [user_query]
)

hotel_emb = model.encode(
    [hotel_review_text]
)

score = cosine_similarity(

    user_emb,

    hotel_emb

)[0][0]

print(score)