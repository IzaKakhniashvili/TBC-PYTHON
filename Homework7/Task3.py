n = int(input("Enter number: "))

while not(n > 0  and n <= 10000):
    n = int(input("Number should be between 0 and 10000: "))
n_sum = n
n_reversed = 0

print("Reversed number is: ", end = "")
while n != 0:
    r = n % 10
    print(r, end = "")
    n = n // 10 
print() 

sum_of_digits = 0
while n_sum != 0:
    r = n_sum % 10
    sum_of_digits += r
    n_sum = n_sum // 10
    
print(f"Sum of digits: {sum_of_digits}")