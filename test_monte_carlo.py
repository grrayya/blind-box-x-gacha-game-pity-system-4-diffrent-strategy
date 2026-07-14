from monte_carlo import simulate_pity_distribution

def test_simulation_pipeline():
    trials = 50
    data = simulate_pity_distribution(trials=trials)
    
    assert len(data) == trials
    assert all(pulls > 0 for pulls in data)
    assert max(data) <= 30  # Hard pity limit means no one should exceed 30 pulls
