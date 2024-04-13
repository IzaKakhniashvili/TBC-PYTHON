import random

def random_list() -> list:
    a = []
    for i in range(0, 10):
        n = random.randint(0, 100)
        a.append(n)
    return a

def n_sum(a: list, b: list, c: list) -> list:
    lists = [a, b, c]
    longest_list = max(lists, key = len)
    list_of_sums = []
    for i in range(0, len(longest_list)):
        n = a[i] + b[i] + c[i]
        list_of_sums.append(n)
    return list_of_sums

def main():
    a = random_list()
    b = random_list()
    c = random_list()
    res = n_sum(a, b, c)
    print(a)
    print(b)
    print(c)
    print(res)


if __name__ == "__main__" :
    main()
        