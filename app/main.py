from fastapi import FastAPI
from students.router import students_router
from users.router import user_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",  # Example for local development
    "https://your-frontend-domain.com",  # Add your frontend's domain here
    # You can also use '*' to allow all origins, but be cautious with that
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
print("hi")
app.include_router(students_router)
app.include_router(user_router)
