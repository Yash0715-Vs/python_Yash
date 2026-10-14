
# from fastapi import FastAPI

# # Create FastAPI application
# app = FastAPI()


# # Home route
# @app.get("/")
# def home():
#     return {"message": "Welcome to FastAPI"}


# # About route
# @app.get("/about")
# def about():
#     return {
#         "name": "Yash",
#         "technology": "Python FastAPI",
#     }

# @app.get("/Student")
# def student():
#     return {
#         "name": "Yash",
#         "college": "Indus University",
#         "technology": "FastAPI"
#     }


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {
#         "user_id": user_id,
#         "message": "User details fetched"
#     }



# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/products")
# def get_product(name: str, price: int = 0):
#     return {
#         "name": name,
#         "price": price
#     }


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/students")
# def get_student(
#     name: str,
#     age: int,
#     course: str = "Python"
# ):
#     return {
#         "name": name,
#         "age": age,
#         "course": course
#     }



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Define the expected request data
class product(BaseModel):
    name: str
    price: float
    quantity: int


# Create a student
@app.post("/product")
def create_product(product: product):
    return {
        "message": "product recive successfully",
        "product": product
    }
