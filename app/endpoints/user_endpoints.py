from fastapi import APIRouter, Depends, HTTPException
from crud.user import Auth as us
from schemas.user_schema import UserCreate, UserUpdate, UserBase


router = APIRouter()


@router.get("/")
def healthcheck():
    return {"message": "success"}


@router.get("/{username}", tags=['User'], response_model=UserBase)
async def get_user(username: str, auth: us = Depends()):
    db_user = await auth.get_user_by_username(username=username)
    return db_user


# @router.post("/", response_model=user_schema.UserBase, status_code=201)
# async def create_user(user: user_schema.UserBase, auth: us = Depends()):
#     db_user = await auth.get_user_by_id(id=user.id)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return auth.create_user(user=user)


@router.post("/", response_model=UserBase, status_code=201)
async def create_user(user: UserCreate, auth: us = Depends()):
    db_user = await auth.get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return auth.create_user(user=user)


@router.patch("/{username}", response_model=UserUpdate)
async def update_user_by_username(username: str, req: UserUpdate, auth: us = Depends()):
    update_user = await auth.update_user_by_username(req, username)
    return update_user


# @router.patch("/{user_id}", response_model=UserUpdate)
# async def update_user_by_id(user_id: int, req: UserUpdate, auth: us = Depends()):
#     update_user = await auth.update_user_by_id(req, user_id)
#     return update_user


@router.delete("/{username}", tags=['User'], status_code=200, response_model=str)
async def delete_user(username: str, auth: us = Depends()):
    db_user = await auth.delete_user_by_username(username)
    if db_user:
        auth.delete_user_by_username(username)
        return f"User successfully deleted"
    raise HTTPException(status_code=400, detail="User not found")
