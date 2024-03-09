
n = input("Enter number between 0 and 50: ")

if n.isdigit():
    n = int(n)
    if n > 0 and n < 50:
        for i in range(1, n + 1):
            count = 0
            divisors = ""
            for j in range(1, i + 1) :
                if i % j == 0:
                    count += 1
                    divisors += str(j) + " "
                    if count == 3:
                        break
            print(f"{i}: {divisors}")
    else:
        print("Invalid input, enter number between 0 and 50.")
else:
    print("Input should be an integer.")      
                     
                    