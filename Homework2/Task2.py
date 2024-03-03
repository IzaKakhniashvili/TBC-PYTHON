a = int(input("Enter number: "))
b = int(input("Enter number: "))


if a > 0 and b > 0:
    if a % b == 0:
        print( a + " is the multiple of " + b)
    else :
        print( a + " is not the multiple of " + b)
else:
    print("Invalid input.")