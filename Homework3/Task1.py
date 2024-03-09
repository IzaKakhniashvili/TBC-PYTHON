import math


a = int(input("Enter number: "))
b = int(input("Enter the power of " + a + " : "))

if b > 0:
    c = math.pow(a, b)
    print(a + " raised to the power b: " + c )
else:
    print("Invalid input.")
