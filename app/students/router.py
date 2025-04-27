from fastapi import APIRouter, HTTPException,Depends
from config.database import db
from students.schemas import StudentSchema, UpdateStudentSchema,StudentListQuery
from students.controller import list_students_controller
# from students.fakedata import generate_fake_student
from bson import ObjectId
from fastapi.responses import StreamingResponse
import pandas as pd
import io


students_router = APIRouter(prefix="/students", tags=["Students"])


collection = db["students"]


@students_router.get("/download", summary="Download Students Data as Excel", tags=["Students"])
async def download_students(query: StudentListQuery = Depends()):
    # Reuse your list_students_controller to fetch data
    data = await list_students_controller(query)
    students = data["data"]

    if not students:
        raise HTTPException(status_code=404, detail="No students found to download.")

    # Remove _id if you don't want it in Excel
    for student in students:
        student.pop("_id", None)

    # Convert list of dicts to pandas DataFrame
    df = pd.DataFrame(students)

    # Write to an in-memory bytes buffer
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Students")
    output.seek(0)

    # Return as file download
    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": f"attachment; filename=students_data.xlsx"
        }
    )



@students_router.post("/")
async def create_student(student: StudentSchema):
    result = await collection.insert_one(student.dict())
    return {"id": str(result.inserted_id)}
# @students_router.post("/insert")
# async def insert_fake_students():
#     n=100
#     students = [generate_fake_student() for _ in range(n)]
#     result = await collection.insert_many(students)
#     return {"inserted_ids": [str(id) for id in result.inserted_ids]}

@students_router.get("/")
async def list_students(query:StudentListQuery=Depends()):
    
    data = await list_students_controller(query)    
    
    return data
    # return students 

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


