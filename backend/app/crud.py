from sqlalchemy.orm import Session
from . import models, schemas, auth

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not auth.verify_password(password, user.hashed_password):
        return None
    return user

def create_product(db: Session, product: schemas.ProductCreate):
    db_p = models.Product(**product.dict())
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p

def list_products(db: Session, skip=0, limit=100):
    return db.query(models.Product).offset(skip).limit(limit).all()
