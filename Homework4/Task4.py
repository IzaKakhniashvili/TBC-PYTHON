#mimdevroba: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

n = input("Enter number: ")
x = 0
lastN = 1

if n.isdigit():
    n = int(n)
    if n >= 0 and n <= 30:
        for i in range (0, n + 1):
            if i == 0:
                lastN = 0
            elif i == 1:
                lastN = 1
            else:
                lastX = lastN
                lastN = lastN + x
                x = lastX    
        print(lastN)
    else:
        print("n should be between 0 and 30.")
else:
    print("Input should be an integer.")
            