friends_dict = {}

while True:
    text = input("enter: ")
    
    if text == "FINISH":
        break
    
    person1, person2 = text.strip().split(' - ')
    
    if person1 not in friends_dict:
        friends_dict[person1] = set()
        
    if person2 not in friends_dict :
        friends_dict[person2] = set()
        
    friends_dict[person1].add(person2)
    friends_dict[person2].add(person1)
    
    
for person, friends in friends_dict.items():
    print(f"{person} -", end = ' ')
    for i in friends:
        print(f"{i}", end = ', ')
    print()
    
  