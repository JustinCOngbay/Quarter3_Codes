import numpy as np

names = ["Me", "Lia", "Jake"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

all_totals = []

for i in range(3):
  sum_monday = 0
  for j in range(3):
    sum_monday += steps[j][0]
  sum_tuesday = 0
  for j in range(3):
    sum_tuesday += steps[j][1]
  sum_wednesday = 0
  for j in range(3):
    sum_wednesday += steps[j][2]
  sum_thursday = 0
  for j in range(3):
    sum_thursday += steps[j][3]
  sum_friday = 0
  for j in range(3):
    sum_friday += steps[j][4]

all_totals.append([sum_monday, sum_tuesday, sum_wednesday, sum_thursday, sum_friday])
highest_steps = max(all_totals[0])
day_index = all_totals[0].index(highest_steps)


for i in range(5):
  print(f"Total steps on {days[i]}: {all_totals[0][i]}")
print(f"Highest steps were on {days[day_index]} with {highest_steps} steps.")



