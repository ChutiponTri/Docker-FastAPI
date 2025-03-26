from fastapi import APIRouter
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
import os

mongo_client = MongoClient(os.getenv("DB_ADDRESS"))
router = APIRouter()

class Users(BaseModel):
    hn: str         # Hospital Number
    age: float
    height: float
    weight: float
    bmi: float

# Function to Create New User
@router.post("/post/users")
async def create_user(data: Users):
    database = mongo_client[os.getenv("DB_NAME")]
    collection = database[os.getenv("DB_USER_COLLECTION")]

    query = {"hn": data.hn}
    exist_user = collection.find_one(query)
    if exist_user:
        response = {"status": "ok", "message": "User Already Exist"}
        return response
    
    collection.insert_one(data.model_dump())
    response = {"status": "ok", "message": "Created User Successfully"}
    return response

class Database(BaseModel):
    hn: str
    x: float
    y: float
    z: float
    visibility: float

# Function to Create New Data
@router.post("/post/database")
async def post_users(data: Database):
    database = mongo_client[os.getenv("DB_NAME")]
    collection = database[os.getenv("DB_DATA_COLLECTION")]
    collection.insert_one(data.model_dump())
    response = {"status": "ok", "message": "Inserted Successfully"}
    return response



