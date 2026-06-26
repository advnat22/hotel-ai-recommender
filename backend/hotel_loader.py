import json

with open(

    "hotel_data.json",

    encoding="utf-8"

) as f:

    hotels=json.load(f)

print(

    "Hotels:",

    len(hotels)

)

print(

    hotels[0]

)