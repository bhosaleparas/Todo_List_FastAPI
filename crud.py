from sqlalchemy.orm import Session
import models
import schemas
from auth import get_password_hash
from typing import List, Optional

# User CRUD operations
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Todo CRUD operations
def get_todo(db: Session, todo_id: int, user_id: int):
    return db.query(models.Todo).filter(
        models.Todo.id == todo_id,
        models.Todo.user_id == user_id
    ).first()

def get_todos(
    db: Session, 
    user_id: int, 
    skip: int = 0, 
    limit: int = 100,
    completed: Optional[bool] = None
):
    query = db.query(models.Todo).filter(models.Todo.user_id == user_id)
    
    if completed is not None:
        query = query.filter(models.Todo.completed == completed)
    
    return query.offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_todo = models.Todo(**todo.dict(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate, user_id: int):
    db_todo = get_todo(db, todo_id, user_id)
    if not db_todo:
        return None
    
    update_data = todo_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = get_todo(db, todo_id, user_id)
    if not db_todo:
        return False
    
    db.delete(db_todo)
    db.commit()
    return True