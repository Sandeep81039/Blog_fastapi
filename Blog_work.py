from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session


from database import get_db
import models
import schemes
from auth import verify_token

router = APIRouter()


@router.post("/create", response_model=schemes.BlogResponce)
def create_Blog(  Blog: schemes.BlogCreate, db: Session = Depends(get_db),user = Depends(verify_token)):
    new_blog = models.Blog(
        title=Blog.title,
        contant=Blog.contant
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog




@router.get("/get_blog/{id}")
def get(id:int,db:Session = Depends(get_db)):
    find_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not find_blog:
       raise  HTTPException(status_code=404,detail="Blog not register with this id or Invalid id")
    return find_blog

@router.delete("/delete/{id}")
def delete_blog(id:int,db:Session = Depends(get_db),user = Depends(verify_token)):
    Blog_find = db.query(models.Blog).filter(models.Blog.id == id).first()
    if Blog_find:
        db.delete(Blog_find)
        db.commit()
        return {
            "message":"Data deleted successfully"
        }
    return {
        "messege":"User not found"
    }

@router.put("/update/{id}")
def update_Blog(id:int,title:str,contant:str,db:Session = Depends(get_db),user = Depends(verify_token)):
    BLog_find = db.query(models.Blog).filter(models.Blog.id == id).first()
    if BLog_find:
        BLog_find.title = title
        BLog_find.contant = contant
        db.commit()
        db.refresh(BLog_find)
        return {
            "message":"Data updated successfully"
        }
    return {
        "message":"User not find"
    }

@router.get("/get_all")
def get_all(db:Session = Depends(get_db),page:int = 1,limit:int = 5):
    skip = (page-1)*10
    Blog_all = db.query(models.Blog).offset(skip).limit(limit).all()
    total_data = db.query(models.Blog).count()
    return ({
        "total data":total_data,
        "data limit":limit,
        "data":Blog_all
    })
    






