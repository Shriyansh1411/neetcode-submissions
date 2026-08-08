class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        res=-1
        right=len(nums)-1
        res=-1
        while left<=right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            elif nums[mid]>=nums[left]:
                if not( target>=nums[left] and target<=nums[mid] ):
                    left=mid+1
                else:
                    right=mid-1
            elif nums[mid]<nums[left]:
                if not (target <= nums[right] and target>=nums[mid]):
                    right=mid-1
                else:
                    left=mid+1
        return res