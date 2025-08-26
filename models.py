from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = None
    created_at: datetime

class DataItem(BaseModel):
    title: str
    content: str
    metadata: Optional[Dict[str, Any]] = None

class DataItemResponse(BaseModel):
    id: str
    title: str
    content: str
    metadata: Optional[Dict[str, Any]] = None
    user_id: str
    created_at: datetime
    updated_at: datetime

class DataItemUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class AuthResponse(BaseModel):
    access_token: str
    user: UserResponse