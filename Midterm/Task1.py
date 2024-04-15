name = input("Enter your name:")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

while not age.isdigit():
    age = input("Enter your age: ")
    
print(f"Hello {name} {surname}")
print(f"Age: {age}")