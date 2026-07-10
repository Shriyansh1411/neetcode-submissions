class Solution:
    def trap(self, height: List[int]) -> int:

        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        water=0
        while left<right:
            if leftmax>rightmax:
                right-=1
                if rightmax>height[right]:
                    water=water+rightmax-height[right]
                else:
                    rightmax=height[right]

            else:
                left+=1
                if leftmax>height[left]:
                    water=water+leftmax-height[left]
                else:
                    leftmax=height[left]
        return water