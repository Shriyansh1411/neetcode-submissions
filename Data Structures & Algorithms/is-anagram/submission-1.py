class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1={}             #character:count
        f2={}

        for i in s:
            f1[i] = f1.get(i, 0) + 1
        for j in t:
            f2[j]= f2.get(j,0)+1
        return f1==f2
        