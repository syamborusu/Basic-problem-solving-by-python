def isanagram(s:str,t:str):
    if len(s)!=len(t):
        return False
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -=1
    for count in freq.values():
        if count !=0:
            return False
    return True
s="aaabca"
t="aaacba"
print(isanagram(s,t))
#TC=O(n) 
#SC=O(k) NO.OF UNIQUE CHARACTER