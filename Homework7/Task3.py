n = int(input("Enter number: "))

while not(n > 0  and n <= 10000):
    n = int(input("Number should be between 0 and 10000: "))

n_reversed = 0

while n != 0:
    r = n % 10
    n_reversed = n_reversed * 10 + r
    n = n // 10 
    
print(n_reversed)

