a = int(input("Enter a: "))
b = int(input("Enter b: "))

def min(a, b):
    if a < b:
        min = a
    else:
        min = b
        
    return min


def find_gcd(a,  b):
    c = min(a, b)
    for i in range(c, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
        
    return gcd


gcd = find_gcd(a, b)    
print(f"GCD of {a} and {b}: {gcd}")