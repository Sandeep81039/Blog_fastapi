from fastapi import FastAPI,APIRouter
import models
from database import engine
from Blog_work import router as work_route
from user_register import route as user_route
app = FastAPI()

app.include_router(work_route)
app.include_router(user_route)

models.Base.metadata.create_all(bind = engine)


