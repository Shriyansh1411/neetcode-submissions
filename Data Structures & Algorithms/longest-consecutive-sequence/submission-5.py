class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for i in s:
            count=1
            if (i-1 in s):
                continue
            else:
                start=i
                while (start+1 in s):
                    if (start+1 in s):
                        start=start+1
                        count+=1
                    else:
                        break
                longest=max(longest,count)
        return longest
