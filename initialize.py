from database import SessionLocal, create_tables
from models import SourceToken
from token_service import generate_token


def seed_data():
    session = SessionLocal()
    try:
        if session.query(SourceToken).count() == 0:
            sap_entry = SourceToken(source="SAP", token=generate_token())
            exo_entry = SourceToken(source="EXO", token=generate_token())
            admin = SourceToken(source="ADMIN", token="03cabdfc-06ce-48ef-b17f-0bb83b120858")
            session.add_all([sap_entry, exo_entry, admin])
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def initialize():
    create_tables()
    seed_data()

