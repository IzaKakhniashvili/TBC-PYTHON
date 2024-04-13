import random

def generate_list() -> list:
    a = []
    for i in range(0, 10):
        n = random.randint(0, 10)
        a.append(n)
    return a

def main():
    a = generate_list()
    shortest = min(a)
    longest = max(a)
    print(shortest, longest)
    a.sort()
    print(a)
    a.reverse()
    print(a)


if __name__ == "__main__" :
    main()
    