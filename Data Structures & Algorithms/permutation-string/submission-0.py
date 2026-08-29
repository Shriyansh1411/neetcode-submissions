class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        hashmap={}
        hmap={}
        l1=len(s1)
        l2=len(s2)
        r=l1
        for i in range(l1):
            hashmap[s1[i]]=hashmap.get(s1[i],0)+1
        for j in s2[l:r:] :
            hmap[j]=hmap.get(j,0)+1
        while r<l2:
            if hmap==hashmap:
                return True
            hmap[s2[l]]-=1
            if hmap[s2[l]]==0:
                del hmap[s2[l]]
            l=l+1
            hmap[s2[r]]=hmap.get(s2[r],0)+1
            r+=1
        if hmap==hashmap:
            return True
        return False
        