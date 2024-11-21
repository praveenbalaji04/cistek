from fastapi import APIRouter, HTTPException
from core.validation import BaseUser
from fastapi import status

from core.models import User

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: BaseUser) -> BaseUser:

    BaseUser.validation(user)

    user_json = user.model_dump()
    user_id = User().add_document(user_json)

    user_obj = User().get_document(user_id)
    return BaseUser(**user_obj).model_dump()


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: str) -> dict:

    user_obj = User().get_document(user_id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    return user_obj


@router.get("/users", status_code=status.HTTP_200_OK)
def users_list() -> list:
    return User().filter({})


@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: str, user: BaseUser) -> dict:

    user_json = user.model_dump()
    User().update_document(user_id, user_json)

    user_obj = User().get_document(user_id)
    return user_obj


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):

    user_obj = User().get_document(user_id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    User().delete_document(user_id)
