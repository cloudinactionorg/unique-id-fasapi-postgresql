from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

engine = create_engine(settings.POSTGRESQL_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()