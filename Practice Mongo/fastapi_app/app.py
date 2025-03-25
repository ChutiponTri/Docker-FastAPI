from fastapi import FastAPI
from dotenv import load_dotenv
from api_get import get
from api_post import post

load_dotenv()
app = FastAPI()
app.include_router(get.router)
app.include_router(post.router)

# Function to GET hello Root
@app.get("/hello")
def get_hello():
    return {"message": "Hello"}

# Function to GET Specific ID
@app.get("/item/{id}")
def get_item(id):
    return {"item": id}
