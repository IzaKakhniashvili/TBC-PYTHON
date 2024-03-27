n = int(input("Enter number greater than 1: "))

while not n > 1:
    n = input("Number should be greater than 1. Enter again: ")
    
x = 0
plus_minus = 1
for i in range(1, n + 1):
    x += plus_minus * (1 / (2 * i - 1))
    plus_minus = plus_minus * -1
    
x = x * 4

print(f"x = {x}")
