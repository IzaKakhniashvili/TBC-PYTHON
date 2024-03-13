import random

MAX_TRIES = 10

num = random.randint(0, 100)
print(f"{num}")

    
user_num = int(input("Enter the number: "))
tries = 1
 
while user_num != num: 
    if tries == MAX_TRIES:
        print("You are out of tries. Computer is the winner.")
        break
    elif user_num > num:
        print("High")
    elif user_num < num:
        print("Low")
    else:
        break
    user_num = int(input("Wrong, enter again: "))
    tries += 1
    
if  user_num == num:
    print("You are the winner.")  