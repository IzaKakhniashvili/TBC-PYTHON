import random

def generate_list():
    a = []
    for i in range(4):
        n = random.randint(1, 5)
        a.append(n)
    return a

def modify_list(a: list) -> list:
    b = []
    for i in a:
        for j in range(i):
            b.append(i)
    return b

def main():
    rand_list = generate_list()
    res = modify_list(rand_list)
    print(f"Size of list: {len(res)}, List: {res}")

if __name__ == "__main__" :
    main()
        