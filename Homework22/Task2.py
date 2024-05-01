import json

my_dict = {}

def user_max_product(filename):
    with open(filename, "r") as file:
        for line in file:
            max_quantity = 0
            split_line = line.strip().split(',')
            quantity = float(split_line[2])
            user = split_line[0]
            if quantity > max_quantity:
                max_quantity = quantity
                my_dict["User maximum quantity"] = user
            
            
def user_max_cost(filename):
     with open(filename, "r") as file:
        for line in file:
            max_cost = 0
            split_line = line.strip().split(',')
            total = float(split_line[2]) * float(split_line[3])
            user = split_line[0]
            if total > max_cost:
                max_cost = total
                my_dict["User maximum cost"] = user
            
def  avg_total_cost(filename):
    with open(filename, "r") as file:
        sum = 0
        counter = 0
        for line in file:
            split_line = line.strip().split(',')
            total = float(split_line[2]) * float(split_line[3])
            sum += total
            counter += 1
        average = sum / counter
        my_dict["Average total cost"] = average
        
def avg_quantity(filename):
    with open(filename, "r") as file:
        sum = 0
        counter = 0
        for line in file:
            split_line = line.strip().split(',')
            total = float(split_line[2])
            sum += total
            counter += 1
        average = sum / counter
        my_dict["Average quantity"] = average
        
def most_bought(filename):
    new_dict = {}
    with open(filename, "r") as file:
        for line in file:
            split_line = line.strip().split(',')
            product = split_line[1]
            amount = float(split_line[2])
            if product in new_dict:
                new_dict[product] += amount
            else:
                new_dict[product] = amount
    most_bought_pr = max(new_dict, key = new_dict.get)
    my_dict["Most wanted product"] = most_bought_pr
    
    
def main():
    user_max_product("/Users/izakakhniashvili/Desktop/python/TBC-PYTHON/Homework22/data.txt")
    user_max_cost("/Users/izakakhniashvili/Desktop/python/TBC-PYTHON/Homework22/data.txt")
    avg_total_cost("/Users/izakakhniashvili/Desktop/python/TBC-PYTHON/Homework22/data.txt")
    avg_quantity("/Users/izakakhniashvili/Desktop/python/TBC-PYTHON/Homework22/data.txt")
    most_bought("/Users/izakakhniashvili/Desktop/python/TBC-PYTHON/Homework22/data.txt")
    with open("new_data.txt.json", "w") as file:
        json.dump(my_dict, file, indent=4)
    
if __name__ == "__main__":
    main()
    