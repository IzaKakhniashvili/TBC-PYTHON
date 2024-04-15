n = int(input("Enter number between 100 and 1000: "))


if not (n >= 100 and n < 1000):
    print("Wrong number.")
else: 
    counter = 0
    for i in range(1, n):
        if i % 13 == 0:
            print(i, end = " ")
            counter += 1
    print()
    print(f"Amount: {counter}")