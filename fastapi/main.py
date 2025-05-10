from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Dict, Any

app= FastAPI()

class Demo(BaseModel):
    id: int
    name: str
    city: str
    
demos: List[Demo] = []

@app.get("/")
def root():
    return {"msg": "Welcome to FastApi"}

@app.get("/demo", response_model= List[Demo])
def get_demo():
    return demos

@app.post("/demo", response_model = Dict[str, Any], status_code = status.HTTP_201_CREATED)
def add_demo(demo: Demo):
    if any(d.id == demo.id for d in demos):
        raise HTTPException(status_code=400, detail="Demo with this ID already exists.")
    
    demos.append(demo)
    return { "msg": "new demo added", "data": demos}

@app.put("/demo/{demo_id}", response_model = Dict[str, Any])
def update_demo(demo_id: int, demo_data: Demo):
    for index, demo in enumerate(demos):
        if demo.id == demo_id:
            demos[index] = demo_data
            return {"msg": "update successfully", "data": demos}
    raise HTTPException(status_code= 404, detail="Demo not found")

@app.delete("/demo/{demo_id}", response_model = Dict[str, Any])
def delete_demo(demo_id: int):
    for index, demo in enumerate(demos):
        if demo.id == demo_id:
            dlt = demos.pop(index)
            return {"msg": "delete success", "data": dlt}
    raise HTTPException(status_code=404, detail="Demo not found")