import random

class BlindBoxSeries:
    def __init__(self, series_name, charm_pool, drop_weights, pity_max):
        self.series_name = series_name
        self.charm_pool = charm_pool
        self.drop_weights = drop_weights
        self.pity_max = pity_max
        self.rarities = list(charm_pool.keys())

    def roll_drop(self, current_pity):
        if current_pity + 1 >= self.pity_max:
            rarity = "Secret Rare"
        else:
            rarity = random.choices(self.rarities, weights=self.drop_weights, k=1)[0]
            
        charm = random.choice(self.charm_pool[rarity])
        return rarity, charm

class UserSession:
    def __init__(self, username):
        self.username = username
        self.stash = {}
        self.pity_tracker = 0

    def open_box(self, series):
        rarity, charm = series.roll_drop(self.pity_tracker)
        
        self.pity_tracker += 1
        if rarity == "Secret Rare":
            self.pity_tracker = 0
            
        if charm in self.stash:
            self.stash[charm] += 1
        else:
            self.stash[charm] = 1
            
        print(f"{self.username} got: [{rarity}] {charm}")
        return charm

if __name__ == "__main__":
    bunny_series = BlindBoxSeries(
        series_name="Polymer Clay Bunnies Vol 1",
        charm_pool={
            "Common": ["Strawberry Bunny", "Matcha Bunny", "Blueberry Bunny"],
            "Rare": ["Cloud Bunny", "Galaxy Bunny"],
            "Secret Rare": ["Golden Crown Bunny"]
        },
        drop_weights=[75, 20, 5],
        pity_max=30
    )

    rayya = UserSession("Rayya")
    abir = UserSession("Abir")

    for _ in range(5):
        rayya.open_box(bunny_series)
    
    abir.open_box(bunny_series)
