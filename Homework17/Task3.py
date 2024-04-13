l = ["apple", "book", "notebook", "first", "banana", "car", "one", "two", "yes", "no"]

def filter_list(a: list) -> list:
    b = []
    for i in a:
        if len(i) <= 3:
            b.append(i)
    return b


def main():
    res = filter_list(l)
    print(l)
    print(res)


if __name__ == "__main__" :
    main()
    