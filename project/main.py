from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class IPL(BaseModel):
    team_id : int
    name : str
    city : str
    players : List[str]
    
    class Config:
        extra = "forbid"

teams: List[IPL] = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the IPL Teams API"}

@app.get("/teams")
def get_teams():
    return teams

@app.post("/add-team")
def add_team(team : IPL):
    for existing_team in teams:
        if (existing_team.team_id == team.team_id or existing_team.name == team.name):
            return {"error": "team already exists"}
    teams.append(team)
    return team
    
@app.put("/team/{team_id}")
def update_team(team_id : int, updated_team: IPL):
        for index, team in enumerate(teams):
            if (team.team_id == team_id):
                teams[index] = updated_team
                return updated_team
        return {"error": "team not found"}
    

@app.delete("/delete-team/{team_id}")
def delete(team_id: int):
    for index, team in enumerate(teams):
        if team.team_id == team_id:
            deleted_team = teams.pop(index)
            return deleted_team
    return {"error": "team not found"}
    print(f"{team_id}")

    