from fastapi import APIRouter
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional
import os

mongo_client = MongoClient(os.getenv("DB_ADDRESS"))
router = APIRouter()

# Function to convert ObjectId to string
def serialize_object_id(obj):
    if isinstance(obj, ObjectId):
        return str(obj)  # Convert ObjectId to string
    elif isinstance(obj, dict):
        return {key: serialize_object_id(value) for key, value in obj.items()}  # Recursively process dicts
    elif isinstance(obj, list):
        return [serialize_object_id(item) for item in obj]  # Recursively process lists
    return obj

# Function to Retrieve Existing User
@router.get("/get/user")
async def get_user(hn: str):
    database = mongo_client[os.getenv("DB_NAME")]
    collection = database[os.getenv("DB_USER_COLLECTION")]
    query = {"hn": hn}
    data = list(collection.find(query))
    response = {"status": "ok", "data": serialize_object_id(data)}
    return response

# Function to Retrieve All Users
@router.get("/get/all/users")
async def get_users():
    database = mongo_client[os.getenv("DB_NAME")]
    collection = database[os.getenv("DB_USER_COLLECTION")]
    data = list(collection.find())
    response = {"status": "ok", "data": serialize_object_id(data)}
    return response

# Function to Retrieve Data
@router.get("/get/database")
async def get_data(
    hn: Optional[str] = None,
    x: Optional[float] = None,
    y: Optional[float] = None,
    z: Optional[float] = None,
    visibility: Optional[float] = None
):
    database = mongo_client[os.getenv("DB_NAME")]
    collection = database[os.getenv("DB_DATA_COLLECTION")]
    query = {key: val for key, val in locals().items() if key != "database" and key != "collection" and val is not None}
    data = list(collection.find(query, {"_id": 0}))                 # Exclude `_id`
    response = {"status": "ok", "data": serialize_object_id(data)}
    return response
