from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/notices")


@router.post(
    "",
    # response_model=schemas.Schedule
)
async def create():
    return f"this is"


@router.get(
    "",
    # response_model=schemas.Schedule
)
async def create():
    return f"this is"


@router.patch(
    "",
    # response_model=schemas.Schedule
)
async def create():
    return f"this is"


@router.delete(
    "",
    # response_model=schemas.Schedule
)
async def create():
    return f"this is"
