from pydantic import BaseModel



class Schedule(BaseModel):
    title: str
    date: str


class EmailBase(BaseModel):
    to: str
    subject: str
    text: str
    # from: str

class EmailCreate(EmailBase):
    pass

class AiChat(BaseModel):
    text: str

class AiChatCreate(AiChat):
    pass

# class ItemBase(BaseModel):
#     title: str
#     description: Union[str, None] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id = int


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True
