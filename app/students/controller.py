
from fastapi import APIRouter, HTTPException,Depends
from students.schemas import StudentListQuery

VALID_SORT_FIELDS = {"name", "rank", "course", "degree", "community", "dateOfAdmission"}

from config.database import db
collection = db["students"]


async def list_students_controller(query: StudentListQuery):
    search = query.search
    sort_by = query.sort_by
    sort_dir = query.sort_dir
    limit = query.limit
    page = query.page
    community = query.community

    # Validate sort_by field
    if sort_by and sort_by not in VALID_SORT_FIELDS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field: {sort_by}. Valid fields are: {', '.join(VALID_SORT_FIELDS)}"
        )

    # Pagination
    skip = (page - 1) * limit

    # Query building
    mongo_query = {}

    if search:
        mongo_query["$or"] = [
            {"name": {"$regex": search, "$options": "i"}},
            {"rank": {"$regex": search, "$options": "i"}},
            {"course": {"$regex": search, "$options": "i"}},
        ]

    if community:
        mongo_query["community"] = community

    # Sorting
    sort = []
    if sort_by:
        direction = -1 if sort_dir == "desc" else 1
        sort = [(sort_by, direction)]

    # Count total
    total_count = await collection.count_documents(mongo_query)
    total_pages = (total_count + limit - 1) // limit  # cleaner formula

    # Fetch students
    students_cursor = collection.find(mongo_query).skip(skip).limit(limit)
    if sort:
        students_cursor = students_cursor.sort(sort)

    students = []
    async for student in students_cursor:
        student["_id"] = str(student["_id"])  # Convert ObjectId to string
        students.append(student)

    # Check if next page exists
    has_next_page = page < total_pages
    
    return {
        "paging": {
            "total_count": total_count,
            "total_page": total_pages,
            "current_page": page,
            "has_next_page": has_next_page,
        },
        "data": students
    }
