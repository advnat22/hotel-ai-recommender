import json

from ollama import chat


with open(
    "processed_hotels.json",
    encoding="utf-8"
) as f:
    hotels = json.load(f)


for hotel in hotels:

    reviews = hotel.get(

        "reviews",

        []

    )

    review_text = ""

    for review in reviews[:5]:

        try:

            review_text += (

                review["text"]["text"]

                + "\n"

            )

        except:

            pass

    if review_text.strip() == "":

        hotel["summary"] = (

            "Not enough reviews available."

        )

        continue

    response = chat(

        model="llama3.2",

        messages=[

            {

                "role":"user",

                "content":f"""

You are summarizing hotel reviews.

Write a short paragraph describing:

1. What guests liked
2. Any complaints
3. Who the hotel is suitable for

Keep it under 80 words.

Reviews:

{review_text}

"""

            }

        ]

    )

    hotel["summary"] = (

        response["message"]["content"]

    )

    print(

        "Done:",

        hotel["displayName"]["text"]

    )


with open(

    "processed_hotels.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        hotels,

        f,

        indent=4,

        ensure_ascii=False

    )

print(

    "Finished generating summaries"

)
