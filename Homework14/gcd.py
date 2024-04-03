a = int(input("Enter a: "))
b = int(input("Enter b: "))


def find_gcd(a,  b):
     if b == 0:
        return a
     else:
        return find_gcd(b, a % b)


gcd = find_gcd(a, b)    
print(f"GCD of {a} and {b}: {gcd}")