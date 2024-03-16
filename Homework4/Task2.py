import random


n = (input("Enter n: "))

_max = 0
if n.isdigit(): #will check if input is integer.
    n = int(n) #will cast str n to int n.
    if n > 0  and n < 30 : 
        for i in range(n):
            a = random.randint(0, 1000)
            print(a)
            if a > _max:
                _max = a
        print(f"Max is: {_max}")
    else:
        print("Please enter a value of n between 1 and 30.")
else:
    print("Enter integer.")
    

