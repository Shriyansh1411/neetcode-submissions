class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        if len(s)!=len(t):
            return False

        else:
            for i in s:
                hashmap[i]=hashmap.get(i,0)+1

        for j in t:
            if j not in hashmap:
                return False
                break
            hashmap[j]-=1
            if hashmap[j]<0:
                return False
                break
        return True