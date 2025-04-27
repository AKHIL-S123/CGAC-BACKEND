from fastapi import FastAPI
from students.router import students_router
from users.router import user_router

app = FastAPI()
print("hi")
app.include_router(students_router)
app.include_router(user_router)
