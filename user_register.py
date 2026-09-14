from fastapi import APIRouter,Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import UserRegister
from auth import password_hash,password_verify,create_token
from fastapi.security import OAuth2PasswordRequestForm
import schemes

route = APIRouter()


def check_user(username:str,db):
   user =  db.query(UserRegister).filter(UserRegister.username == username).first()
   if user:
       return True
   return False

@route.post("/User_Register")
def User_register(new_user:schemes.UserRegister,db:Session = Depends(get_db)):
  if  check_user(new_user.username,db):
     raise HTTPException(status_code=409,detail="User already register with this username")
  new_user = UserRegister(
     username = new_user.username,
     password = password_hash(new_user.password) )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return({
     "message":"User successfully register",
     "Username":new_user.username
  })

@route.post("/get_token")
def get_token(form_data:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
   if not check_user(form_data.username,db):
      raise HTTPException(status_code=404,detail="User not found")
   user_find = db.query(UserRegister).filter(UserRegister.username == form_data.username).first()
   if not password_verify(form_data.password,user_find.password):
      raise HTTPException(status_code=401, detail="Incorrect password")
   token = create_token({
      "sub":form_data.username
   })
   return {
    "access_token": token,
    "token_type": "bearer"
} 
   
   
   

  
  
  
