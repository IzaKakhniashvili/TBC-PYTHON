#ranks:  2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(11), Queen(12), King(13), Ace(1).
#suits: Hearts(1), Diamonds(2), Spades(3), Clubs(4).

import random


random_rank = random.randint(1, 13)
random_suit = random.randint(1, 4)

if random_rank == 1:
    rank = "Ace"
elif random_rank == 11:
    rank = "Jack"
elif random_rank == 12:
    rank = "Queen"
elif random_rank == 13:
    rank = "Ace"
else:
    rank = random_rank

if random_suit == 1:
    suit = "Hearts"
elif random_suit == 2:
    suit = "Diamonds"
elif random_suit == 3:
    suit = "Spades"
else:
    suit = "Clubs"

print(f"Random card is: {rank} of {suit}.")
