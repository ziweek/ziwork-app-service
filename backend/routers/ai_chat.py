from fastapi import APIRouter, HTTPException
from services import openai_chat

# from models import schemas
from models import schemas

router = APIRouter(prefix="/api/v1/ai-chat")


@router.post(
    "",
    # response_model=schemas.Schedule
)
async def create(ai_chat_create: schemas.AiChatCreate):
    created_ai_chat = openai_chat.ai_chat(ai_chat_create)
    if not created_ai_chat:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"result": True, "message": created_ai_chat}


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
