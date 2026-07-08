class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]
        for i in range (0,len(nums)-1-1):
            left=i+1
            right=len(nums)-1
            while (left < right):
                if nums[left]+nums[right]+nums[i]>0:
                    right-=1
                elif nums[left]+nums[right]+nums[i]<0:
                    left+=1
                elif nums[left]+nums[right]+nums[i]==0:
                    if ([nums[left],nums[right],nums[i]] not in output):
                        output.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1
        return output