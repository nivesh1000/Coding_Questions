from collections import defaultdict
def isIsomorphic(s: str, t: str) -> bool:
    d=defaultdict(str)
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=t[i]
        else:
            if d[s[i]] !=t[i]:
                return False
    d2=defaultdict(str)
    for i in range(len(t)):
        if t[i] not in d2:
            d2[t[i]]=s[i]
        else:
            if d2[t[i]] !=s[i]:
                return False        
    return True
print(isIsomorphic('abc','ded') )