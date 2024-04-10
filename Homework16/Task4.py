def merge_list(a: list, b: list) -> list:
    c = a + b
    return c


def sort_list(a: list) -> list:
    for i in range(1, len(a)):
        n = a[i]
        j = i - 1
        while j >= 0 and n < a[j]:
            a[j + 1] = a[j]
            j -= 1
            a[j + 1] = n
    return a

def main():
    a = [1, 3, 10]
    b = [0, 4, 7, 9]
    c = merge_list(a, b)
    res = sort_list(c)
    print(f"{a} and {b} merged and sorted {res}")
    
    
if __name__ == "__main__" :
    main()
