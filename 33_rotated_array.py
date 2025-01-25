def search(nums, target):
    e=len(nums)-1
    m=int(e/2)
    b=0
    if nums[m]==target:
        return m
    if nums[b]==target:
        return b
    if nums[e]==target:
        return e 
    while(b<e):
        m=int((e+b)/2)
        if nums[m]==target:
            return m
        if nums[b]==target:
            return b
        if nums[e]==target:
            return e              
        dif_b=abs(nums[b]-target)
        dif_m=abs(nums[m]-target)
        dif_e=abs(nums[e]-target)
        min_dif=min(dif_b,dif_e,dif_m)
        if min_dif==dif_b:
            e=m-1
        elif min_dif==dif_e:   
            b=m+1
        else:
            if target>nums[m]:
                b=m+1
            else:
                e=m-1         
    return -1 


print(search([4,5,6,7,0,1,2], 1))


