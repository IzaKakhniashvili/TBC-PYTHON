import math


a = float(input("შეიყვანეთ სამკუტხედის გვერდი: "))
b = float(input("შეიყვანეთ სამკუტხედის გვერდი: "))
c = float(input("შეიყვანეთ სამკუტხედის გვერდი: "))

p = a + b + c
halfp = p / 2
s = math.sqrt(halfp * (halfp - a) *(halfp - b) * (halfp - c))

print("სამკუთხედის პერიმეტრია: " + str(p))
print("სამკუთხედის ფართობია: " + str(s))

# s = (halfp * (halfp - a) *(halfp - b) * (halfp - c)) ** 0.5

