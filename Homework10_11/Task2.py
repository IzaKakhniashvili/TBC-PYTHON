import random
import math

n = int(input("Enter number greater than 1: "))

while not n > 1:
    n = input("Number should be greater than 1. Enter again: ")
    
counter = 0
for i in range(n):
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    if math.sqrt(a ** 2 + b ** 2) <=1:
        counter += 1
        
rslt = 4 * counter / n

print(f"Result: {rslt}")