from random import randint

def rev(arr, k):
    arrs = [arr[i:i+k] for i in range(0, len(arr), k)]

    res = []

    for chunk in arrs:
        i = 0
        j = len(chunk) - 1
        while i < j:
            chunk[i], chunk[j] = chunk[j], chunk[i]
            i += 1
            j -= 1

        res += chunk

    return res


if __name__ == '__main__':
    arr = [randint(0, 100) for _ in range(0,randint(5,20))]

    print(arr)
    print(rev(arr, 3))