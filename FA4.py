import numpy as np

names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

total_steps = []

for i in range(3):
    print(f"{names[i]}'s steps: {steps[i]}")
    total_steps.append(sum(steps[i]))
    print(f"Total steps for {names[i]}: {total_steps[i]}")

highest_steps = max(total_steps)
lowest_steps = min(total_steps)
difference = highest_steps - lowest_steps
print(f"Highest total steps: {highest_steps}")
print(f"Lowest total steps: {lowest_steps}")
print(f"Difference between highest and lowest: {difference}")