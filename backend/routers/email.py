from fastapi import APIRouter, HTTPException
from services import google_gmail

# from models import schemas
from models import schemas

router = APIRouter(prefix="/api/v1/emails")


@router.post(
    "",
    # response_model=schemas.Schedule
)
async def create(email_create: schemas.EmailCreate):
    print(email_create)
    created_mail = google_gmail.gmail_send_message(email_create)
    if created_mail:
        raise HTTPException(status_code=400)
    return {"result" : True}


# @router.get(
#     "",
#     # response_model=schemas.Schedule
# )
# async def create():
#     return f"this is"


# @router.patch(
#     "",
#     # response_model=schemas.Schedule
# )
# async def create():
#     return f"this is"


# @router.delete(
#     "",
#     # response_model=schemas.Schedule
# )
# async def create():
#     return f"this is"
