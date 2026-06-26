weights={

"Low":1,

"Medium":2,

"High":3
}


def hotel_score(

    hotel,

    pref

):

    score=(

        hotel["rating"]

        +

        hotel["food"]

        *

        weights[pref["food"]]

        +

        hotel["transport"]

        *

        weights[pref["transport"]]

        +

        hotel["luxury"]

        *

        weights[pref["luxury"]]

        +

        hotel["cleanliness"]

        *

        weights[pref["cleanliness"]]

    )

    return score