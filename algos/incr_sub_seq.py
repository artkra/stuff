def incsum(nums):
    sumlist = nums[:]
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[j] < nums[i] and nums[i] + sumlist[j] > sumlist[i]:
                sumlist[i] = nums[i] + sumlist[j]
    
    print(sumlist)

    return max(sumlist)


if __name__ == '__main__':
    arr = [1, 101, 2, 3, 100, 4, 5]

    print(incsum(arr))