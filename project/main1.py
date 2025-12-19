from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    secretIdentity: str
    powers: List[str]

data = [
  {
    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
    "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
  },
  {
    "name": "Madame Uppercut",
    "age": 39,
    "secretIdentity": "Jane Wilson",
    "powers": ["Million tonne punch", "Damage resistance", "Superhuman reflexes"]
  },
  {
    "name": "Eternal Flame",
    "age": 1000000,
    "secretIdentity": "Unknown",
    "powers": ["Heat generation", "Fire resistance", "Invulnerability"]
  }
]

@app.get("/")
async def getInitData():
    return {"message": "Hey there, How are you doing?"}

@app.get("/data/reveal_identity")
async def reveal_identity():
    return data

@app.get("/get-user/{name}")
async def greet(name: str):
    for person in data:
        if (person["name"] == name):
            return person
    return {"error": "Person not found"}
        
@app.post("/add-user")
async def add_user(user: User):
    # new_user = user.dict()
    print(user)
    print(user.dict())
    data.append(user.dict())
    return {"message": "User added successfully", "user": user}