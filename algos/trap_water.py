from random import randint

def trap_water(arr, n):
    res = 0

    for bar in arr:
        if n - bar > 0:
            res += n - bar
    return res


if __name__ == '__main__':
    arr = [randint(0, 6) for _ in range(randint(1, 10))]
    print(arr)
    n = 5
    print(n)
    print(trap_water(arr, n))