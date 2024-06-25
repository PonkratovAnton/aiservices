from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base


class SourceToken(Base):
    __tablename__ = "source_tokens"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, unique=True, index=True)
    token = Column(String, unique=True, index=True)


class RequestModel(BaseModel):
    user_input: str


class ResponseModel(BaseModel):
    response: str


class TokenResponseModel(BaseModel):
    token: str
