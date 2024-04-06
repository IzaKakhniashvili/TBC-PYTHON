def count_vowels(a: str) -> int:
    vowels = "aeiuouAEIOU"
    counter = 0
    for i in a:
        if i in vowels:
            counter += 1
    return counter

def main():
    print("Test -> ", count_vowels('Test'))
    print("Python -> ", count_vowels('Python'))
    print("Kvaratskhelia -> ", count_vowels('Kvaratskhelia'))
    

if __name__ == "__main__" :
    main()