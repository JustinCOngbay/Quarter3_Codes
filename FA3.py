import numpy as np

prices = [["apple", 30], ["banana", 20],["orange", 25]]

for i in range(3):
    print(prices[i]) 
    
total = sum([price[1] for price in prices])
print(f"Total price so far: {total}")

average = np.mean([price[1] for price in prices])
print(f"Average price so far: {average}")