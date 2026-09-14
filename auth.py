from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from fastapi import HTTPException,Header,Depends




ALGORITHMS = "HS256"
SECRET_KEY = "DEEEP"
pwt_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="get_token")



def password_hash(password:str):
    return pwt_context.hash(password)

def password_verify(plain_p:str,hash_p:str):
    return pwt_context.verify(plain_p,hash_p)


def create_token(data:dict):
    payload = data.copy()
    expire_time = datetime.now(timezone.utc)+timedelta(minutes=30)
    payload.update({
        "exp":expire_time
    })
    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHMS)
    return token

def verify_token(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHMS])
        return payload
    except JWTError:
        raise  HTTPException(status_code=401,detail="Either expire or invalid token")
    
    
    



