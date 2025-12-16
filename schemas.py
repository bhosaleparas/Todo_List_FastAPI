from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    
    

class UserCreate(UserBase):
    password: str
    
    
    

class UserLogin(BaseModel):
    username: str
    password: str
    
    
    

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True



class UserInDB(User):
    hashed_password: str
    




# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    
    

class TokenData(BaseModel):
    username: Optional[str] = None
    
    

# Todo Schemas
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False



class TodoCreate(TodoBase):
    pass



class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None



class Todo(TodoBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True