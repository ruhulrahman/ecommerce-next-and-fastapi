from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL database URL
# DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/ecommerce"
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/fastapi_db_test"

# Example:
# username = root
# password = 123456
# database = ecommerce

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
