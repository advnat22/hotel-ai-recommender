from pydantic import BaseModel


class UserCreate(BaseModel):

    email:str

    password:str



class PreferenceCreate(BaseModel):

    user_id:int

    budget:str

    trip_type:str

    food:str

    transport:str

    luxury:str

    cleanliness:str