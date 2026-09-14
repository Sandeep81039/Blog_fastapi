from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    contant:str


class BlogResponce(BaseModel):
    id:int
    title: str
    contant:str

class Config:
    from_attributes = True


class UserRegister(BaseModel):
    username:str
    password:str

class UserResponce(BaseModel):
    username:str


