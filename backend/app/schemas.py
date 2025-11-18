from pydantic import BaseModel, EmailStr
from typing import Optional, List
import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class ProductBase(BaseModel):
    name: str
    price: float
    
class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ProductCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    stock: int = 0

class ProductOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: float
    stock: int
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    product_ids: List[int]

class OrderOut(BaseModel):
    id: int
    total: float
    created_at: datetime.datetime
    class Config:
        orm_mode = True
