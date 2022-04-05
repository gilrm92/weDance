from fastapi import APIRouter
from users.controllers import userController

router = APIRouter()
router.include_router(userController.router)