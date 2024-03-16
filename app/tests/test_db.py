import os
from contextlib import contextmanager
from typing import Generator

import pytest
from app.src.config.settings import settings
from app.src.utils.constants import BASE_DIR
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


class DBHandler:
    def __init__(self) -> None:
        self.db_name = settings.database_db
        self.db_user = settings.database_user
        self.db_password = settings.database_password
        self.db_host = settings.database_host
        self.db_port = settings.database_port
        self.postgres = f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        self.sqlLite = f"sqlite:///{BASE_DIR}/{settings.database_db}.sqlite3"
        self.db_url = self.postgres if settings.app_env == "production" else self.sqlLite
        self.engine = create_engine(self.db_url, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @contextmanager
    def get_db(self) -> Generator[Session, None, None]:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


db_handler = DBHandler()


@pytest.fixture(scope="module")
def test_db() -> Generator[Session, None, None]:
    db = db_handler.SessionLocal()
    yield db
    db.close()
    if os.path.exists("./test.db"):
        os.remove("./test.db")


def test_get_db(test_db: Session) -> None:
    expected = "Session"
    result = str(type(test_db))
    assert expected in result


def test_get_db_context_manager() -> None:
    with db_handler.get_db() as db:
        expected = "Session"
        result = str(type(db))
        assert expected in result


def test_db_connection() -> None:
    try:
        with db_handler.get_db() as db:
            db.execute(text("SELECT 1"))
    except Exception as e:
        assert False, f"La conexión a la base de datos falló: {e}"
