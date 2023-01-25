from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

POSTGRES_DATABASE_URL = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
SQLITE_DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(POSTGRES_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



