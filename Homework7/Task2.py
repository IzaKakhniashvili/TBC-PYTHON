n = int(input("Enter number between 0 and 1000: "))
last_n = 0
output = str(n)

while not(n > 0  and n <= 1000):
    n = int(input("Number should be between 0 and 1000: "))
    
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n * 3) + 1
    n = int(n)
    output += " -> " + str(n)
    
print(output)