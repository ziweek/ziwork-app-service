# # from typing import List

# # from fastapi import Depends, FastAPI, HTTPException
# # from sqlalchemy.orm import Session

# from fastapi import FastAPI


# from config.connection import SessionLocal

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()


# app.include_router(users.router)
# app.include_router(items.router)

from fastapi import FastAPI

from routers import schedules, notices

# from sqladmin import Admin, ModelView
# from models import models


# from config.database import engine

app = FastAPI()
app.include_router(schedules.router)
app.include_router(notices.router)
# admin = Admin(app, engine)


# class UserAdmin(ModelView, model=User):
#     column_list = [User.id]


# admin.add_view(UserAdmin)


# @app.get("/")
# async def root():
#     return {"message": True}
