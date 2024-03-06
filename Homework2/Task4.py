v = int(input("Enter speed of the car: "))

if v > 0 and v <= 30 :
    print("Category of the speed: SLOW")
elif v > 30 and v <= 60 : 
    print("Category of the speed: MODERATE")
elif v > 60 and v <= 120 :
    print("Category of the speed: FAST")
elif v > 120:
    print("Category of the speed: VERY FAST")
elif v == 0:
    print("Car is not moving.")
else: 
    print("Invalid input.")