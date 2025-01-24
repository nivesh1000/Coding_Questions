def singleNumber(nums) -> int:
    l=len(nums)
    a=0
    for i in range(1,l):
        a=a^nums[i]
    return a
        

print(singleNumber([1,2,2,3,4,4,3,1,9]))   