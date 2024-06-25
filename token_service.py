import uuid

from fastapi import Header, HTTPException

from database import SessionLocal
from models import SourceToken

session = SessionLocal()


def get_token_by_service_name(service_name: str):
    token_entry = session.query(SourceToken).filter(SourceToken.source == service_name).first()
    if token_entry is None:
        return None
    return token_entry.token


def generate_token():
    return str(uuid.uuid4())


def check_token_exists(token: str):
    token_entry = session.query(SourceToken).filter(SourceToken.token == token).first()
    return token_entry is not None


async def verify_token(token: str = Header(...)):
    if not check_token_exists(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    return True


