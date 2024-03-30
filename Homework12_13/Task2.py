a = input("Input a: ")
b = input("Input b: ")

if len(a) != len(b):
    print("Output: NO")
    
for i in range(len(a)):
    new_a = a[len(a) - 1] + a[ : len(a) - 1]
    a = new_a
    if a == b:
        print("Output: YES")
        break
    
if a != b:
    print("Output: NO")
    