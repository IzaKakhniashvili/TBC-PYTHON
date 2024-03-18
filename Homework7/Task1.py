n = int(input("Enter number between 0 and 20: "))

while not(n >= 0  and n <= 20):
    n = int(input("Number should be between 0 and 20: "))
    
#0, 1, 1, 2, 3, 5, 8, 13...

i = 2   #განსაზღვრავს მიმდევრობის წევრის რიგს
last_a = 0
current_a = 1
output = "0, 1, "

if n == 0: 
    output = "0"
elif n == 1:
    output = "0, 1"
else:
    while i < n + 1:
        a = last_a + current_a
        last_a = current_a
        current_a = a
        i += 1
        output = output + str(a) + ", "

print(output)   
