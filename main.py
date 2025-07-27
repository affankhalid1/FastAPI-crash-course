from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Tea(BaseModel):
    id:int 
    name:str
    origin:str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message":"Welcome to chai code."}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return f"This tea is successfully added {tea}"

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int, updated_tea:Tea):
    for i, tea in enumerate(teas):
        if tea["id"] == tea_id:
            teas[i] = updated_tea
            return update_tea
    return {"error":"Invalid Tea ID."}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int):
    for tea in teas:
        if tea.id == tea_id:
            deleted = teas.pop(tea)
            return deleted
    return {"error":"Tea not found"}