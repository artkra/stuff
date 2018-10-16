import random

def equi(arr):
    lo_sum = 0
    hi_sum = 0
    lo = 0
    hi = len(arr) - 1
    
    while hi > lo:
        if lo_sum < hi_sum:
            lo_sum += arr[lo]
            lo += 1 
        else:
            hi_sum += arr[hi]
            hi -= 1

    return(hi_sum, lo_sum)

if __name__ == '__main__':
    arr = [random.randint(0, 2) for _ in range(100)]
    print(arr)

    print(equi(arr))