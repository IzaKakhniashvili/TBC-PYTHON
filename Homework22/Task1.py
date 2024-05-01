

with open("./data.txt", "r") as file:
    with open("small.txt", "w") as sm_file:
        with open("large.txt", "w") as lr_file:   
            for line in file:
                split_line = line.strip().split(',')
                quantity = float(split_line[2])
                price = float(split_line[3])
                total = quantity * price
                if total < 10:
                        sm_file.write(line)
                else: 
                        lr_file.write(line)
                    

        
