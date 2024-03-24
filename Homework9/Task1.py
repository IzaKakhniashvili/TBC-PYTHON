text = input("Input: ")

cleaned_text = ""
for i in text:
    if i.isalpha():
        cleaned_text += i
        
        
cleaned_text = cleaned_text.lower()

if  cleaned_text == cleaned_text[::-1]:
    print("Output: Is palindrome")   
else:
    print("Output: Is not palindrome")