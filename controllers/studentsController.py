import uuid
from fastapi import APIRouter, Body, Depends, status
from models.student import Student
from repositories import studentRepository
router = APIRouter(prefix="/students", tags=["Students"], responses={404: {"description": "Not found"}})


@router.get("/getStudents/")
async def getStudents():
    students = studentRepository.getStudents()
    return students

@router.get("/getStudent/{id}")
async def getStudent(id):
    student = studentRepository.getStudent(id)
    return student

@router.post("/createStudent/", status_code=status.HTTP_201_CREATED)
async def createStudent(student: Student = Body(...)):
    student.id = str(uuid.uuid4())
    studentRepository.saveStudent(student)
    return "Ok"

@router.delete("/deleteStudent/{id}", status_code=status.HTTP_200_OK)
async def deleteStudent(id):
    studentRepository.deleteStudent(id)
    return "Ok"
