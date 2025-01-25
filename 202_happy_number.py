def isHappy(n) -> bool:
    his=[]
    while(n not in his):
        s=str(n)
        his.append(n)
        n=0
        for i in s:
            n+=(int(i)*int(i))
           
        
        if n == 1:
            return True
    return False     
print(isHappy(2))  