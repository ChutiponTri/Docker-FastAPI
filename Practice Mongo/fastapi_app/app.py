from fastapi import FastAPI
from dotenv import load_dotenv
import random
from api_get import get
from api_post import post

load_dotenv()
app = FastAPI()
app.include_router(get.router)
app.include_router(post.router)

# Function to GET Root
@app.get("/")
def get_hello():
    return {"message": "Welcome"}

# Function to GET hello Root
@app.get("/hello")
def get_hello():
    return {"message": "Hello"}

# Function to GET Specific ID
@app.get("/item/{id}")
def get_item(id):
    return {"item": id}

# Function to GET Color
@app.get("/color")
def get_color():
    colors = ["red", "blue", "green", "yellow", "pink", "white", "black"]
    return {"color": random.choice(colors)}

