def maximumGap( nums) -> int:
    nums.sort()
    maxdif=0
    for i in range(1,len(nums)):
        maxdif=max(maxdif,nums[i]-nums[i-1])
    return maxdif


print(maximumGap([1,5,8,4])   ) 