from fastapi.testclient import TestClient
from fastapi_app import app, active_sessions

client = TestClient(app)

def setup_function():
    # Clear between tests
    active_sessions.clear()

def test_new_user_inventory_is_empty():
    res = client.get("/inventory/abir")
    
    assert res.status_code == 200
    data = res.json()
    assert data["stash"] == {}
    assert data["pity_tracker"] == 0

def test_pull_increments_pity_and_stash():
    res = client.post("/pull/abir")
    
    assert res.status_code == 200
    data = res.json()
    
    # If they got incredibly lucky on pull 1, pity resets. 
    if data["rarity"] == "Secret Rare":
        assert data["pity_tracker"] == 0
    else:
        assert data["pity_tracker"] == 1
        
    # Verify the pull was saved to the db state
    assert active_sessions["abir"]["pity_tracker"] == data["pity_tracker"]
    assert data["charm"] in active_sessions["abir"]["stash"]
