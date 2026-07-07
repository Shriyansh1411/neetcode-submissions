class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]      #output = [48,24,12,8]
        prefix=[1]
        suffix=[1]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*nums[i-1])        #   prefix= [1,1,2,8]

        

        rev_nums=nums
        rev_nums.reverse()

        for j in range(1,len(nums)):
            suffix.append(suffix[j-1]*nums[j-1])
        suffix.reverse()      # suffix= [48, 24, 6, 1]

        for k in range(0,len(nums)):
            output.append(prefix[k]*suffix[k])
        return output