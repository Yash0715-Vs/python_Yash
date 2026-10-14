
from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# About route
@app.get("/about")
def about():
    return {
        "name": "Yash",
        "technology": "Python FastAPI"
    }
