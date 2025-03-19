from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import json
import os

load_dotenv()

app = FastAPI()
mongo_client = MongoClient(os.getenv("DB_ADDRESS"))

# Function to convert ObjectId to string
def serialize_object_id(obj):
    if isinstance(obj, ObjectId):
        return str(obj)  # Convert ObjectId to string
    elif isinstance(obj, dict):
        return {key: serialize_object_id(value) for key, value in obj.items()}  # Recursively process dicts
    elif isinstance(obj, list):
        return [serialize_object_id(item) for item in obj]  # Recursively process lists
    return obj

# Function to GET Database
@app.get("/database/{name}")
def get_database_list(name):
    database = mongo_client[os.getenv("DB_NAME")]
    collection = database[os.getenv("DB_COLLECTION")]
    query = {"name": name}
    data = list(collection.find(query))
    data = serialize_object_id(data)
    response = {"status": "ok", "data": data}
    return response

# Function to GET hello Root
@app.get("/hello")
def get_hello():
    return {"message": "Hello"}

# Function to GET Specific ID
@app.get("/item/{id}")
def get_item(id):
    return {"item": id}
