import random
import statistics

class BlindBoxSeries:
    def __init__(self, charm_pool, drop_weights, pity_max):
        self.charm_pool = charm_pool
        self.drop_weights = drop_weights
        self.pity_max = pity_max
        self.rarities = list(charm_pool.keys())

    def roll_drop(self, current_pity):
        if current_pity + 1 >= self.pity_max:
            return "Secret Rare"
        return random.choices(self.rarities, weights=self.drop_weights, k=1)[0]


def simulate_pity_distribution(trials=10000):
    print(f"Simulating {trials:,} users pulling for Secret Rare...")
    
    series = BlindBoxSeries(
        charm_pool={"Common": [], "Rare": [], "Secret Rare": []},
        drop_weights=[75, 20, 5],
        pity_max=30
    )
    
    pulls_to_hit = []
    
    for _ in range(trials):
        boxes_opened = 0
        pity_tracker = 0
        hit_secret = False
        
        while not hit_secret:
            boxes_opened += 1
            rarity = series.roll_drop(pity_tracker)
            
            pity_tracker += 1
            if rarity == "Secret Rare":
                hit_secret = True
                
        pulls_to_hit.append(boxes_opened)
        
    return pulls_to_hit

if __name__ == "__main__":
    distribution_data = simulate_pity_distribution(10000)

    # 94 index maps to 95th percentile in a 100-slice split
    unlucky_threshold = statistics.quantiles(distribution_data, n=100)[94] 

    print(f"Mean pulls: {statistics.mean(distribution_data):.1f}")
    print(f"Median pulls: {statistics.median(distribution_data):.1f}")
    print(f"95% of users finish within: {unlucky_threshold:.1f} pulls")
