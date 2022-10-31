import random

names = [
   "E&A", "R&J", "W&H"
]

godparents = random.randint(0, len(names) - 1)
print(f"Godparents chosen: {names[godparents]}")
