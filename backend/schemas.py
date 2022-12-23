import datetime as _dt
import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):
    email:str

class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True

class User(_UserBase):
    id:int

    class Config:
        orm_mode = True

class _LeadeBase(_pydantic.BaseModel):
    first_name:str
    last_name:str
    email:str
    first_name:str

class LeadCreate(_LeadeBase):
    pass

class Lead(_LeadeBase):
    id:int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        orm_mode = True