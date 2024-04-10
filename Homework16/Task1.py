temp = [22, 25, 19, 23, 25, 26, 23]

def mean_value(a: list) -> int:
    counter = 0
    for i in a:
        counter += i
    mean = counter/len(a)
    return mean
    
def main():
    res = mean_value(temp)
    print(f"Mean value of temperatures: {res}")

if __name__ == "__main__" :
        main()
        