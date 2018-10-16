from random import choice, shuffle


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


def findKMin(arr,k,start=0,end=None):
    '''
    Find kth minimum element in a array (in-place randomized algorithm, similar to quicksort)
    assumption: Input will only contain unique elements'''
    if k > len(arr):
        raise Exception("k should be less than length of the input array")
    if not end: end = len(arr) -1 #Get last index value
    pivot_ridx = choice(list(range(start, end)))     #Get a random array element as pivot value
    pivot = arr[pivot_ridx]
    pivot_idx = partition(arr,start,end,pivot_ridx) #partition to partition array around the pivot value in place
    if pivot_idx+1 == k:
        return pivot #Well, there is your answer
    elif pivot_idx+1 > k:
        return findKMin(arr,k,start,pivot_idx) #lies somewhere in the first partition
    else:
        return findKMin(arr,k,pivot_idx,end) #lies somewhere in the second Partiton

def partition(arr,start,end,pivot_idx):
    '''
    Partitions array in-place around the given pivot value
    '''
    pivot = arr[pivot_idx]
    arr[end],arr[pivot_idx] = arr[pivot_idx],arr[end]
    inc_idx = start
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[inc_idx],arr[i] = arr[i],arr[inc_idx]
            inc_idx+=1
    arr[end],arr[inc_idx] = arr[inc_idx],arr[end]
    return inc_idx

if __name__ == '__main__':
    test_input = list(range(100))
    print(test_input)
    k = 5
    shuffle(test_input)
    print(findKMin(test_input, k))