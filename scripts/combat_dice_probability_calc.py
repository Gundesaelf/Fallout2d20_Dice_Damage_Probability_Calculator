import random
from collections import Counter
from colorama import Fore, init

init()

def roll_cd():
    roll = random.randint(1, 6)
    if roll == 1:
        return 1  # 1 damage
    elif roll == 2:
        return 2  # 2 damage
    elif roll in [3, 4]:
        return 0  # no damage
    elif roll in [5, 6]:
        return 1  # 1 damage + effect
    return 0

def roll_4cd():
    return sum(roll_cd() for _ in range(4)) # Number of cd

results = [roll_4cd() for _ in range(1000)] # Number of sims

damage_counts = Counter(results)

print('\n')

total = sum(damage_counts.values())

for dmg, count in sorted(damage_counts.items()):
    
    percent = (count/total) * 100
    print(Fore.LIGHTCYAN_EX)
    print(f'{dmg} damage: {count} times; {percent:,.0f}%')

print('\n')