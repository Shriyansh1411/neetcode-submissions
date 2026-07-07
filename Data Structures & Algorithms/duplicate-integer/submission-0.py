class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}     #value:index
        for i, n in enumerate(nums):
            if n in  freq:
                return True
            freq[n]=i
        return False