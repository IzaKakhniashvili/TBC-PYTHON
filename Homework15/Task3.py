def string_reverse(a: str) -> str:
    if len(a) <= 1:
        return a
    else:
        return string_reverse(a[1:]) + a[0]
    

def main():
    print("Test ->", string_reverse("Test"))
    print("Abc -> ", string_reverse("Abc"))
    print("String -> ", string_reverse("String")) 
    
if __name__ == "__main__" :
        main()