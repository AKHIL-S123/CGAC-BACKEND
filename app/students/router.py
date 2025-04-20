from fastapi import APIRouter, HTTPException
from config.database import db
from students.schemas import StudentSchema, UpdateStudentSchema
from bson import ObjectId


students_router = APIRouter(prefix="/students", tags=["Students"])
collection = db["students"]

@students_router.post("/")
async def create_student(student: StudentSchema):
    result = await collection.insert_one(student.dict())
    return {"id": str(result.inserted_id)}

@students_router.get("/")
async def list_students():
    students = []
    async for student in collection.find():
        student["_id"] = str(student["_id"])  # Convert ObjectId to string
        students.append(student)
    return students

@students_router.get("/{student_id}")
async def get_student(student_id: str):
    student = await collection.find_one({"_id": ObjectId(student_id)})
    if student:
        student["_id"] = str(student["_id"])  # Convert ObjectId to string
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@students_router.put("/{student_id}")
async def update_student(student_id: str, data: UpdateStudentSchema):
    result = await collection.update_one({"_id": ObjectId(student_id)}, {"$set": data.dict(exclude_unset=True)})
    if result.modified_count:
        return {"message": "Student updated"}
    raise HTTPException(status_code=404, detail="Student not found or nothing changed")

@students_router.delete("/{student_id}")
async def delete_student(student_id: str):
    result = await collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count:
        return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")

