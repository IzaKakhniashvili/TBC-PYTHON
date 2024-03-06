a =  int(input("Enter number between 1 and 10: "))

 #prime numbers between 1 and 10: 2, 3, 5, 7.

if a > 0 and a <= 10 :
    if a % 2 == 0 and a % 3 == 0:
        print("Prime divisors: 2, 3.")
    elif a % 2 == 0 and a % 5 == 0 :
        print("Prime divisors: 2, 5.")
    elif a % 2 == 0 :
        print("Prime divisor: 2.")
    elif a % 3 == 0 :
        print("Prime divisor: 3.")
    elif a % 5 == 0:
        print("Prime divisor: 5.")
    elif a % 7 == 0:
        print("Prime divisor: 7.")
    else: 
        print("No prime divisors.")
else:
    print("Invalid input.")

