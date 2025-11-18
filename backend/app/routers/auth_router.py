from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import crud, schemas, auth, database

# router = APIRouter(prefix="/auth", tags=["auth"])
router = APIRouter(tags=["Auth"])
# router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user = crud.get_user_by_email(db, user_in.email)
    if user:
        raise HTTPException(400, "Email already registered")
    user = crud.create_user(db, user_in)
    return user

@router.post("/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(401, "Incorrect email or password")
    token = auth.create_access_token(subject=str(user.id))
    return {"access_token": token, "token_type": "bearer"}
