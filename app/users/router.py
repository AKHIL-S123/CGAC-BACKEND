from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.database import db
from users.schema import *
from jose import jwt
import datetime
from bson import ObjectId


SECRET_KEY = "your-secret-key"  # make it strong for production
ALGORITHM = "HS256"

# --- Pydantic Models ---
user_router = APIRouter()
  # make sure you have a "users" collection
user_collection =db["users"]

def create_access_token(data: dict, expires_delta: int = 60):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- Login Route ---

@user_router.post("/login", response_model=TokenResponse, tags=["Auth"], summary="Simple login with role encoding")
async def login(login_req: LoginRequest):
    user = await user_collection.find_one({"email": login_req.email})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if login_req.password != user.get("password"):
        raise HTTPException(status_code=401, detail="Incorrect password")

    # Prepare payload
    payload = {
        "sub": str(user["_id"]),
        "role": user.get("role", "user")  # default role "user" if not set
    }

    access_token = create_access_token(data=payload)

    return {"access_token": access_token}







# --- Create User ---

@user_router.post("/users", tags=["Users"], summary="Create new user")
async def create_user(user: UserCreate):
    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    result = await user_collection.insert_one(user.dict())
    return {"message": "User created successfully", "id": str(result.inserted_id)}

# --- Update User ---

@user_router.put("/users/{user_id}", tags=["Users"], summary="Update user")
async def update_user(user_id: str, user: UserUpdate):
    update_data = {k: v for k, v in user.dict().items() if v is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = await user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated successfully"}

# --- Delete User ---

@user_router.delete("/users/{user_id}", tags=["Users"], summary="Delete user")
async def delete_user(user_id: str):
    result = await user_collection.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}


