from fastapi import APIRouter
from controllers import userController, studentsController

router = APIRouter()
router.include_router(userController.router)
router.include_router(studentsController.router)