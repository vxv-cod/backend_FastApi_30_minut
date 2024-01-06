from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import get_db
# from fastapi.responses import JSONResponse

from services import user as UserService
from dto import user as UserDTO

router = APIRouter()

import orjson
from typing import Any

   
@router.post('/', tags=["user"])
# async def create(data: UserDTO.User = None, db: Session = Depends(get_db)):
def create(data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)


@router.get('/', tags=["user"])
# async def get(id: int = None, db: Session = Depends(get_db)):
def get_all(db: Session = Depends(get_db)):
    return UserService.get_user_all(db)


@router.get('/{id}', tags=["user"])
# async def get(id: int = None, db: Session = Depends(get_db)):
def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)


@router.put('/{id}', tags=["user"])
# async def update(data: UserDTO.User = None, id: int = None, db: Session = Depends(get_db)):
def update(data: UserDTO.User = None, id: int = None, db: Session = Depends(get_db)):
    return UserService.update(data, db, id)


@router.delete('/{id}', tags=["user"])
async def delete(id: int = None, db: Session = Depends(get_db)):
# def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove(db, id)
