text = input("Input: ")
print("Output:")

for i in range(len(text)):
    new_text = text[len(text) - 1] + text[ : len(text) - 1]
    print(new_text)
    text = new_text