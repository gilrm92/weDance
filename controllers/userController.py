import uuid
from fastapi import APIRouter, Body, Depends, status
from repositories import userRepository
from models.user import User

router = APIRouter(prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}})

@router.get("/getUser/{id}")
async def getUser(id):
    user = userRepository.getUser(id)
    return user;

@router.post("/createUser/", status_code=status.HTTP_201_CREATED)
async def createUser(user: User = Body(...)):
    user.id = str(uuid.uuid4())
    userRepository.saveUser(user)
    return "Ok"

@router.delete("/deleteUser/{id}", status_code=status.HTTP_200_OK)
async def deleteUser(id):
    userRepository.deleteUser(id)
    return "Ok"