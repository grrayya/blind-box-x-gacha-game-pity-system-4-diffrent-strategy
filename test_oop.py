import pytest
from oop import BlindBoxSeries, UserSession

@pytest.fixture
def mock_series():
    return BlindBoxSeries(
        series_name="Test Pool",
        charm_pool={"Common": ["Trash"], "Rare": ["Okay"], "Secret Rare": ["Grail"]},
        drop_weights=[80, 15, 5],
        pity_max=10
    )

def test_user_pity_resets_on_secret_rare(mock_series):
    rayya = UserSession("Rayya")
    rayya.pity_tracker = 9  # One pull away from max pity
    
    charm = rayya.open_box(mock_series)
    
    assert charm == "Grail"
    assert rayya.pity_tracker == 0
    assert rayya.stash["Grail"] == 1

def test_independent_user_states(mock_series):
    user_a = UserSession("A")
    user_b = UserSession("B")
    
    user_a.open_box(mock_series)
    
    assert user_a.pity_tracker > 0 or user_a.stash.get("Grail")
    assert user_b.pity_tracker == 0
    assert len(user_b.stash) == 0
