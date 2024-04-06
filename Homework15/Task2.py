def is_prime(a: int) -> bool:
    for i  in range(2, a):
        if a % i == 0:
            return False
    return True

def main():
    print("Is 3 prime?", is_prime(3))
    print("Is 17 prime?", is_prime(17))
    print("Is 97 prime?", is_prime(97))
    print("Is 100 prime?", is_prime(100))
        
if __name__ == "__main__" :
        main()