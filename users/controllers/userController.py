from fastapi import APIRouter, Depends, status
from managers import dbManager

from users.models.user import User

router = APIRouter(prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}})

@router.get("/getUser/{id}")
async def getUser(id):
    user = dbManager.getUser(id)
    return user;

@router.post("/createUser/", status_code=status.HTTP_201_CREATED)
async def createUser(user: User = Depends(User)):
    dbManager.saveUser(user)
    return "Ok"

@router.delete("/deleteUser/{id}", status_code=status.HTTP_200_OK)
async def deleteUser(id):
    dbManager.deleteUser(id)
    return "Ok"