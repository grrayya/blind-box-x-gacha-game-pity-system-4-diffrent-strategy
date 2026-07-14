from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PullResult(BaseModel):
    username: str
    rarity: str
    charm: str
    pity_tracker: int

class UserState(BaseModel):
    username: str
    stash: dict[str, int]
    pity_tracker: int


active_sessions = {}

rarities = ["Common", "Rare", "Secret Rare"]
drop_weights = [75, 20, 5]
charm_pool = {
    "Common": ["Strawberry Bunny", "Matcha Bunny", "Blueberry Bunny"],
    "Rare": ["Cloud Bunny", "Galaxy Bunny"],
    "Secret Rare": ["Golden Crown Bunny"]
}
PITY_MAX = 30


@app.get("/inventory/{username}", response_model=UserState)
def fetch_inventory(username: str):
    if username not in active_sessions:
        return {"username": username, "stash": {}, "pity_tracker": 0}
        
    return {
        "username": username, 
        "stash": active_sessions[username]["stash"], 
        "pity_tracker": active_sessions[username]["pity_tracker"]
    }

@app.post("/pull/{username}", response_model=PullResult)
def execute_pull(username: str):
    if username not in active_sessions:
        active_sessions[username] = {"stash": {}, "pity_tracker": 0}
    
    session = active_sessions[username]
    session["pity_tracker"] += 1
    
    if session["pity_tracker"] >= PITY_MAX:
        rarity = "Secret Rare"
    else:
        rarity = random.choices(rarities, weights=drop_weights, k=1)[0]
        
    pulled_charm = random.choice(charm_pool[rarity])
    
    if rarity == "Secret Rare":
        session["pity_tracker"] = 0
        
    if pulled_charm in session["stash"]:
        session["stash"][pulled_charm] += 1
    else:
        session["stash"][pulled_charm] = 1
        
    return {
        "username": username,
        "rarity": rarity,
        "charm": pulled_charm,
        "pity_tracker": session["pity_tracker"]
    }
