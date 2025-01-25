from collections import defaultdict
def majorityElement( nums) -> int:
    count = defaultdict(int)
    for i in nums:
        count[i]+=1
    mx=0
    for i in count.values():
        if i>mx:
            mx=i
    for i,j in count.items():
        if j ==mx:
            return i   
    
    
print(majorityElement([1,2,1,2,1,2,1,2,1,2,1,3,6,3,3,3,3,3,3,3,3,3,3,3]))    