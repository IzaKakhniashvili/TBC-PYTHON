keyboard = "qwertyuiopasdfghjklzxcvbnm"

e_d = input("Enter action (e/d): ")
while e_d != "e" and e_d != "d":
    e_d = input("Enter only e or d: ")
    
word = input("Enter text: ")   
word = word.lower()

if e_d == "e":
    for i  in range(0, len(word)):
        for j in range(0, len(keyboard)):
            if word[i] == keyboard[j]:
                if j == 9:
                    print(keyboard[0], end = " ")
                elif j == 18:
                    print(keyboard[10], end = " ")
                elif j == 26:
                    print(keyboard[19], end = " ")
                else:
                    print(keyboard[j + 1], end = " ")
                    
if e_d == "d":
    for i  in range(0, len(word)):
        for j in range(0, len(keyboard)):
            if word[i] == keyboard[j]:
                if j == 0:
                    print(keyboard[9], end = " ")
                elif j == 10:
                    print(keyboard[18], end = " ")
                elif j == 19:
                    print(keyboard[26], end = " ")
                else:
                    print(keyboard[j - 1], end = " ")
print()               