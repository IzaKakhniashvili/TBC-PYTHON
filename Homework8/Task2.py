word = input("Enter the word: ")
vowels = "aeiou"


for i in word:
    is_vowel = False
    for j in vowels:
        if i == j:
            is_vowel = True
            break
    if not is_vowel:
        print(i, end = " ")
            
print()
