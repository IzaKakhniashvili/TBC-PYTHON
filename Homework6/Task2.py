PASSWORD = "Georgia"
MAX_TRIES = 3

user_password = input("Enter the password: ")

for i in range(1, MAX_TRIES):
    if user_password != PASSWORD:
        user_password = input("Your password was incorrect, enter again: ")
        continue
    else:
        break
        
if user_password != PASSWORD:
    print("You are blocked.")
else:
    print("Hello from Georgia.")