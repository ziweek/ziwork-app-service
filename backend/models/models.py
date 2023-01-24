from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

# from config.database import Base


class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    title = Column(String)
    tag = Column()

    start_time = Column(DateTime)
    end_time = Column(DateTime)

    location = Column(String)
    memo = Column(Text)

class Schedule_Tags(Base):
    __tablename__="schedule_tags"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    key = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


# Base.metadata.create_all(engine)


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), index=True)
#     description = Column(String(255), index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")
