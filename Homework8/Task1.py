word = input("Entyer text: ")

for i in range(len(word)):
    if i % 2 == 1:
        if word[i] != "e":
            print(word[i], end = " ")
print()
            
            
