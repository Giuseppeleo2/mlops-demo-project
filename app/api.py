from fastapi import FastAPI
from app.main import add

app = FastAPI()


@app.get("/add")
def add_endpoint(a: int, b: int):
    return {"result": add(a, b)}
