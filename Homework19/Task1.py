import random
new_dict = {}
even = []
odd = []

for i in range (100):
    n = random.randint(0, 100)
    if n % 2 == 0:
       even.append(n)
    else: 
        odd.append(n)
        
new_dict['even'] = even
new_dict['odd'] = odd

print(new_dict)