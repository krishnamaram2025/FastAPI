'''
This module is intended to create Endpoints for the Hackathon.
'''
import json
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import Optional
from database.db_operations import get_teams, insert_team, delete_team, update_team
from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()
app = FastAPI(title="Hackathon Teams", version="1.0.0",docs_url="/hackathon/api/docs", openapi_url="/hackathon/api/openapi.json", debug=True )

# Create the router object so that we can define the API endpoints
router = APIRouter(prefix="/hackathon/api")

# Add the Middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Create_team(BaseModel):
    team_name: str
    member1: str
    member2: str
    member3: str

class Update_team(BaseModel):
    team_name: str
    member1: str
    
class Delete_team(BaseModel):
    team_name: str


@router.post("/team/create")
def create_team(team: Create_team):
    payload = team.model_dump()
    team = insert_team(payload)
    return {"team_id": team}

@router.get("/teams")
def fetch_teams():
    list_of_teams = get_teams()
    return {"teams": list_of_teams}



@router.put("/team/update")
def team_update(team: Update_team):
    payload = team.model_dump()
    team = update_team(payload)
    return {"team_id": team}

@router.delete("/team/delete")
def team_delete(team: Delete_team):
    payload = team.model_dump()
    team = delete_team(payload)
    return {"team_id": team}

# Include the router in the main FastAPI app
app.include_router(router)

