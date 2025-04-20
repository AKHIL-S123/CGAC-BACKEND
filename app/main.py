from fastapi import FastAPI
from students.router import students_router

app = FastAPI()
print("hi")
app.include_router(students_router)
