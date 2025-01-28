def plusOne(digits):
    s=''
    for i in digits:
        s+=str(i)
    n=int(s)
    n+=1
    s2=str(n)
    lis2=[]
    for i in s2:
        lis2.append(int(i))
    return lis2    
print(plusOne([1,2,3,4,9]))