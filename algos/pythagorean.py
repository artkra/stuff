import random

def find_pyth(arr):
    arr = [x*x for x in arr]
    print(arr)
    for x_el in arr:
        for y_el in arr:
            if x_el + y_el in arr:
                return True, x_el, y_el
    return False


if __name__ == '__main__':
    arr = list(range(1, 10))
    random.shuffle(arr)
    print(arr)
    print(find_pyth(arr))