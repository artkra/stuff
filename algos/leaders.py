from random import randint

def leaders(arr):
    n = len(arr)

    leaders = []

    for i in range(0, n):
        for j in range(i, n):
            if arr[i] < arr[j]:
                break

            if j == n - 1:
                leaders.append(arr[i])
    
    return leaders

if __name__ == '__main__':
    arr = [randint(0, 20) for _ in range(10)]

    print(arr)

    print(leaders(arr))