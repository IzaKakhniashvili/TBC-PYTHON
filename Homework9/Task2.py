print("Input:")
text_1 = input()
text_2 = input()

cleaned_text_1 = ""
for i in text_1:
    if i.isalpha():
        cleaned_text_1 += i

cleaned_text_2 = ""
for i in text_2:
    if i.isalpha():
        cleaned_text_2 += i
        
cleaned_text_1 = cleaned_text_1.lower()
cleaned_text_2 = cleaned_text_2.lower()

srtd_cleaned_text_1 = sorted(cleaned_text_1)
srtd_cleaned_text_2 = sorted(cleaned_text_2)

if srtd_cleaned_text_1 == srtd_cleaned_text_2:
    print("Output: YES")
else:
    print("Output: NO")