from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")


queries=[

    "hotels in Sentosa Singapore",

    "hotels in HarbourFront Singapore"

]

all_hotels=[]

url="https://places.googleapis.com/v1/places:searchText"

headers={

    "Content-Type":"application/json",

    "X-Goog-Api-Key":API_KEY,

    "X-Goog-FieldMask":
    "places.displayName,places.formattedAddress,places.rating,places.reviews"

}

for query in queries:

    payload={

        "textQuery":query

    }

    response=requests.post(

        url,

        headers=headers,

        json=payload

    )

    print("\nQuery:",query)

    print(

        "Status:",

        response.status_code

    )

    print(

        response.json()

    )

    data=response.json()

    if "places" in data:

        all_hotels.extend(

            data["places"]

        )

with open(

    "hotel_data.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        all_hotels,

        f,

        indent=4

    )

print(

    "\nHotels saved:",

    len(all_hotels)

)