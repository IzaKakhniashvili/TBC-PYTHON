word = input("Enter word: ")

word_dict = {}
count = 0

for i in word:
    counter = 0
    if i not in word_dict:
        for j in word:
            if i == j:
                counter += 1
        word_dict[i] = counter
        
for i, j in word_dict.items():
    print(f"{i} - {j}")