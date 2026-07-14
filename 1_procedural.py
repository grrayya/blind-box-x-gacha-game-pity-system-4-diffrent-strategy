import random

rarities = ["Common", "Rare", "Secret Rare"]
drop_weights = [75, 20, 5] 

charm_pool = {
    "Common": ["Strawberry Bunny", "Matcha Bunny", "Blueberry Bunny"],
    "Rare": ["Cloud Bunny", "Galaxy Bunny"],
    "Secret Rare": ["Golden Crown Bunny"]
}

stash = {}
pity_tracker = 0
PITY_MAX = 30

def pull_box():
    global pity_tracker, stash
    
    pity_tracker += 1
    
    if pity_tracker >= PITY_MAX:
        pulled_rarity = "Secret Rare"
    else:
        pulled_rarity = random.choices(rarities, weights=drop_weights, k=1)[0]
    
    pulled_charm = random.choice(charm_pool[pulled_rarity])
    
    # reset on hit so they don't double dip
    if pulled_rarity == "Secret Rare":
        pity_tracker = 0
        
    if pulled_charm in stash:
        stash[pulled_charm] += 1
    else:
        stash[pulled_charm] = 1
        
    return pulled_rarity, pulled_charm

if __name__ == "__main__":
    for _ in range(10):
        rarity, charm = pull_box()
        print(f"[{rarity}] {charm}")

    print("\nFinal Stash:", stash)
