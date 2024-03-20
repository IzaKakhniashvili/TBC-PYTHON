word = input("Enter the word: ")

i = 0

while i < 5:
    print(word[0], end = " ")
    i += 1
print(", " , end = "")

i = 0    
while i < 5:
    n = len(word) // 2
    if len(word) % 1 == 1:
        print(word[n], end = " ")
    else:
        print(word[n - 1], word[n], end = " ")
    i += 1
print(", " , end = "")

i = 0  
while i < 5:
    n = len(word) - 1
    print(word[n], end = " ")
    i += 1
print(", " , end = "")

print()
        
        
    
        
        