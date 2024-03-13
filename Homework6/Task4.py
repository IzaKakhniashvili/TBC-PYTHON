n = int(input("Enter the number: "))

while not(n > 0 and n <10):
    n = int(input("Number should be between 0 and 10. Enter again: "))
    
a = 0

while a < n :
    i = 0
    while i < a + 1:
        print(i + 1, end =" ")
        i += 1
    print()
    a += 1
    
while a > 0:
     i = 0
     while i < a:
         print(i + 1, end=" ")
         i += 1
     print()
     a -= 1