'''
This module is intended to create Endpoints for the portfolio.
'''
import json
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import Optional
from database.db_operations import get_skills, insert_skill, delete_skill, update_skill
from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()
app = FastAPI(title="Portfolio skills", version="1.0.0",docs_url="/portfolio/api/docs", openapi_url="/portfolio/api/openapi.json", debug=True )

# Create the router object so that we can define the API endpoints
router = APIRouter(prefix="/portfolio/api")

# Add the Middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Create_skill(BaseModel):
    skill_name: str
    stream_name: str

class Update_skill(BaseModel):
    skill_name: str
    stream_name: str
    
class Delete_skill(BaseModel):
    skill_name: str


@router.post("/skill/create")
def create_skill(skill: Create_skill):
    payload = skill.model_dump()
    skill = insert_skill(payload)
    return {"skill_id": skill}

@router.get("/skills")
def fetch_skills():
    list_of_skills = get_skills()
    return {"skills": list_of_skills}



@router.put("/skill/update")
def skill_update(skill: Update_skill):
    payload = skill.model_dump()
    skill = update_skill(payload)
    return {"skill_id": skill}

@router.delete("/skill/delete")
def skill_delete(skill: Delete_skill):
    payload = skill.model_dump()
    skill = delete_skill(payload)
    return {"skill_id": skill}

# Include the router in the main FastAPI app
app.include_router(router)

