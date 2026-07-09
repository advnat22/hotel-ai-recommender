import json

from nlp_engine import analyze_review

with open(
    "hotel_data.json",
    encoding="utf-8"
) as f:
    hotels = json.load(f)

processed = []

for hotel in hotels:

    reviews = hotel.get(
        "reviews",
        []
    )

    food = 0
    transport = 0
    luxury = 0
    clean = 0
    sentiment = 0
    count = 0

    for review in reviews:

        text = review.get(
            "text",
            {}
        ).get(
            "text",
            ""
        )

        if text == "":
            continue

        result = analyze_review(text)

        food += result["food"]
        transport += result["transport"]
        luxury += result["luxury"]
        clean += result["cleanliness"]
        sentiment += result["sentiment"]

        count += 1

    if count == 0:
        count = 1

    processed.append({

        "name":
        hotel["displayName"]["text"],

        "address":
        hotel.get(
            "formattedAddress",
            ""
        ),

        "rating":
        hotel.get(
            "rating",
            0
        ),

        "food":
        round(
            food / count,
            2
        ),

        "transport":
        round(
            transport / count,
            2
        ),

        "luxury":
        round(
            luxury / count,
            2
        ),

        "cleanliness":
        round(
            clean / count,
            2
        ),

        "sentiment":
        round(
            sentiment / count,
            2
        ),

        "summary":
        hotel.get(
            "summary",
            "Summary unavailable"
        )

    })

with open(
    "processed_hotels.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        processed,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    "Processed:",
    len(processed)
)
