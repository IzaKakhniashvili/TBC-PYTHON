n = input("Enter number: ")


if n.isdigit():
    n = int(n)
    if n > 0:
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end = " ")
    else:
        print("Invalid input. Enter positive integer.")
else:
    print("Invalid input. Enter integer.") 
    
    
    
    