from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class API(BaseModel):
    id: int
    name: str
    origin: str


apis: list[API] = []

@app.get("/")
def read_root():
    return {"message:" "Welcome to my first API"}

@app.get("/apis")
def get_apis():
    return apis

@app.post("/apis")
def add_api(requests: API):
    apis.append(requests)
    return requests

@app.put("/apis/{api_id}")
def update_api(api_id: int, updated_api: API):
    for index, api in enumerate(apis):
        if api.id == api_id:
            apis[index] = updated_api
            return updated_api
    return{"error": "API not found"}

@app.delete("/apis/{api_id}")
def delete_api(api_id: int):
    for index, api in enumerate(apis):
        if api.id == api_id:
            deleted = apis.pop(index)
            return deleted
    return{"error": "API not found"}    


