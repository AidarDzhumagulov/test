from fastapi import APIRouter, Depends, HTTPException
from crud.user import UserCrud
from db.database import DbSession
from schemas.user_schema import UserCreate, UserUpdate, UserBase


router = APIRouter()


@router.get("/")
def healthcheck():
    return {"message": "success"}


@router.get("/{username}", tags=['User'], response_model=UserBase)
async def get_user(username: str, user_crud: UserCrud = Depends()):
    async with DbSession() as db:
        db_user = await user_crud.get_user_by_username(username=username, db=db)
    return db_user


@router.post("/", response_model=UserBase, status_code=201)
async def create_user(user: UserCreate, user_crud: UserCrud = Depends()):
    async with DbSession() as db:
        db_user = await user_crud.get_user_by_username(username=user.username, db=db)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        return await user_crud.create_user(user=user, db=db)


@router.patch("/{username}", response_model=UserUpdate)
async def update_user_by_username(username: str, req: UserUpdate, user_crud: UserCrud = Depends()):
    async with DbSession() as db:
        update_user = await user_crud.update_user_by_username(req, username, db)
    return update_user


@router.delete("/{username}", tags=['User'], status_code=200, response_model=str)
async def delete_user(username: str, user_crud: UserCrud = Depends()):
    async with DbSession() as db:
        result = await user_crud.delete_user_by_username(username, db=db)
        if result:
            return f"User successfully deleted"
    raise HTTPException(status_code=400, detail="User not found")
