import random

n = input("Enter the number of players: ")

if n.isdigit():
    n = int(n)
    if n > 0:
        for i in range(n):
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            print(f"Dices for the player {i + 1}: {dice_1, dice_2}")
    else:
        print("Number of players should be postive.")
else:
    print("Input should be integer.")
