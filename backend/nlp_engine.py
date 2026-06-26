from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()


food_words=[

    "food",

    "restaurant",

    "breakfast",

    "buffet",

    "dining",

    "meal",

    "eat",

    "cafe",

    "bar"

]


transport_words=[

    "mrt",

    "station",

    "transport",

    "location",

    "bus",

    "walk",

    "walking",

    "accessible",

    "near",

    "distance"

]


luxury_words=[

    "luxury",

    "premium",

    "spa",

    "resort",

    "pool",

    "beach",

    "view",

    "beautiful",

    "relaxing",

    "exclusive"

]


clean_words=[

    "clean",

    "cleanliness",

    "tidy",

    "hygiene",

    "dirty",

    "smell",

    "fresh",

    "maintained",

    "room service",

    "towels"

]



def keyword_score(

    review,

    words

):

    score=0

    review=review.lower()

    for word in words:

        if word in review:

            score+=1

    return score



def analyze_review(

    review

):

    review=review.lower()

    sentiment=analyzer.polarity_scores(

        review

    )["compound"]


    return {

        "sentiment":

        sentiment,

        "food":

        keyword_score(

            review,

            food_words
        ),

        "transport":

        keyword_score(

            review,

            transport_words
        ),

        "luxury":

        keyword_score(

            review,

            luxury_words
        ),

        "cleanliness":

        keyword_score(

            review,

            clean_words
        )

    }