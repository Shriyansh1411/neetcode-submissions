class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l, r,  maxlen=0,0,0
        hashmap={}  #character:index
        while r<n:
            if s[r] not in hashmap:
                hashmap[s[r]]=r
                maxlen=max(maxlen,r-l+1)
            elif s[r] in hashmap:
                l=max(l,hashmap[s[r]]+1)
                hashmap[s[r]]=r
                maxlen=max(maxlen,r-l+1)
            r+=1

        return maxlen