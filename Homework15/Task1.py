def convert_temp(a: str, b: int) -> float:
    if a == "C":
        temp = b * 9/5 + 32
    else:
        temp = (b - 32) * 5/9
    return temp


def main():
    print("20 Celsius in Fahrenheit is ",  convert_temp("C", 20))
    print("68 Fahrenheit in Celsius is ", convert_temp("F", 68))
    print("100 Celsius in Fahrenheit is ",  convert_temp("C", 100))
    print("212 Fahrenheit in Celsius is ", convert_temp("F", 212))
    
    
if __name__ == "__main__" :
        main()
        
