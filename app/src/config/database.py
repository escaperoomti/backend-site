from typing import Generator

from app.src.config.settings import settings
from app.src.utils.constants import BASE_DIR
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if settings.app_env == "test":
    DATABASE_URL = f"sqlite:///{BASE_DIR}/{settings.database_db}.sqlite3"
else:
    DATABASE_URL = f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_db}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
