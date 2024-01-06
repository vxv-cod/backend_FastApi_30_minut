from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_URL = "postgresql+psycopg2://SapsanPlusUser:SapsanPlusUserqwe123@tnnc-sapsan-db:5432/SapsanPlus"
SQLALCHEMY_URL = "sqlite:///foo.db"

engine = create_engine(
    SQLALCHEMY_URL, 
    # connect_args={"check_same_tread": False},
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        