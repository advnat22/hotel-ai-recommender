from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from database import Base


class User(Base):

    __tablename__="users"

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    email=Column(
        String,
        unique=True
    )

    password=Column(
        String
    )



class Preference(Base):

    __tablename__="preferences"

    id=Column(
        Integer,
        primary_key=True
    )

    user_id=Column(
        Integer,
        ForeignKey(
            "users.id"
        )
    )

    budget=Column(String)

    trip_type=Column(String)

    food=Column(String)

    transport=Column(String)

    luxury=Column(String)

    cleanliness=Column(String)