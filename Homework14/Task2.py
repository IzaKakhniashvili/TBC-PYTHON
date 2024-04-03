from gcd import find_gcd

a = int(input("Enter a: "))
b = int(input("Enter b: "))

lcm = int((a * b)/find_gcd(a, b))
print(f"LCM of {a} and {b} is {lcm}")


