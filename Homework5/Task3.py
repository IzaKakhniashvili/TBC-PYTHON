n = input("Enter the height of the tree: ")

#    *          *          *
#   /|\         |         /|\
#  //|\\                 //|\\
#    |                  ///|\\\  
#                          |   

if n.isdigit():
    n = int(n)
    if n > 0 and n < 50:
        for i in range (1, n + 1):
            space = " " * (n - i)
            branches = "/" * (i - 1) + "|" + "\\" * (i - 1)
            if i == 1:
                branches = "*"
            elif i == n:
                space = " " * (i - 1)
                branches = "|"
            
            print(space + branches)
    else:
        print("Enter number between 0 and 50.")
else:
    print("Input should be an integer.")
        
        
