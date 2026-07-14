# blind-box-x-gacha-game-pity-system-4-diffrent-strategy

1. **`procedural.py`** — The bare bones. Just a quick script that rolls the dice and prints what you got.
2. **`oop.py`** — Better organization. This version lets two different players keep track of their own separate stashes and pity counters at the same time.
3. **`monte_carlo.py`** — The math test. This script creates 10,000 fake players and opens boxes for them until they win. It tells us the exact average of how lucky/unlucky people actually are.
4. **`fastapi_app.py`** — The web server. This takes all our rules and turns them into a real backend that a website can talk to.
5. **`index.html`** — The frontend. A cute, interactive website where you can actually click a button to open boxes and see your stash grow.

## why i built 
my friend was talking about how gacha games had her hooked and now she is super into blind boxes but wishes that like in gacha games there was a pity system fro secrets depending on how much you buy 
and i agreed with her, it would nice to be garennted a "secret" at some point, so i made a program simlar to do this idea and as like a flexable porhect i made diffrent versions and such. 

## How to Run

**Prerequisites:** Python 3.9+

Run the standalone scripts directly:
```bash
python 1_procedural.py
python 2_oop.py
python 3_monte_carlo.py
