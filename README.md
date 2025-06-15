# Fallout2d20_Dice_Damage_Probability_Calculator

This Python script simulates rolling a custom 6-sided die four times, calculates the damage based on specific rules, and summarizes the distribution of total damage over 1000 simulations.

## How It Works

- The custom die has the following damage outcomes per roll:
  - Roll 1: 1 damage
  - Roll 2: 2 damage
  - Rolls 3 or 4: 0 damage
  - Rolls 5 or 6: 1 damage + special effect (counted as 1 damage here)
- Each simulation rolls the die 4 times and sums the damage.
- Runs 1000 such simulations.
- Prints the frequency and percentage distribution of total damage values.

## Requirements

- Python 3.x
- `colorama` for colored terminal output

Install `colorama` via pip if needed:

```bash
pip install colorama
```

## Usage

Run the script from your command line:

```bash
python dice_simulator.py
```

You will see output like:

```
0 damage: 123 times; 12%
1 damage: 345 times; 35%
2 damage: 289 times; 29%
3 damage: 200 times; 20%
4 damage: 43 times; 4%
```

(distribution numbers will vary per run)

## Notes

- The script uses `colorama` for colored output — works best on terminals that support ANSI colors.
- You can adjust the number of simulations by changing the `range(1000)` in the code.
- The simulation logic can be adapted easily for different dice or damage rules.

---

Feel free to customize this script to model other dice-based damage mechanics!

---


## 🔗 Connect with me https://www.linkedin.com/in/chris-gundes
