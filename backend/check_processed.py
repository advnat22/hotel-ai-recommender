import json

with open(

    "processed_hotels.json",

    encoding="utf-8"

) as f:

    hotels=json.load(f)

print(

    hotels[0]

)