from fastapi import FastAPI  # pyright: ignore[reportMissingImports]

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}  