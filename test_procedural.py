import procedural

def setup_function():
    # wipe before each test
    procedural.stash = {}
    procedural.pity_tracker = 0

def test_pity_system_triggers():
    procedural.pity_tracker = 29
    
    rarity, charm = procedural.pull_box()
    
    assert rarity == "Secret Rare"
    assert procedural.pity_tracker == 0  # Should reset after hit

def test_stash_tracks_items():
    procedural.pull_box()
    procedural.pull_box()
    
    total_charms = sum(procedural.stash.values())
    assert total_charms == 2
