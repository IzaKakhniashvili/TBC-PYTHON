import random

comp = "RPS"
#R -> 1, P -> 2, S -> 3

def generate_rps():
    n = random.randint(0, 2)
    return comp[n]


    
comp_rps = generate_rps()
user_rps = input("Rock, Paper, Scissor. Enter R/P/S: ")
print(f"Computer RPS: {comp_rps}.")
res = comp_rps + user_rps

if res == "RS" or res == "SP" or res == "PR":
    print("Computer is the winner.")
elif res == "SR" or res == "PS" or res == "RP":
    print("User is the winner.")
else:
    print("Nobody is the winner.")