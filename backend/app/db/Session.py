from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

POSTGRES_DATABASE_URL = "postgresql://postgres@password:postgresuser/testdb"
SQLITE_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLITE_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



