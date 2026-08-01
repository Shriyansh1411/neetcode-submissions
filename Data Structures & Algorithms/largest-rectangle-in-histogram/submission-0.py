class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0 
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                element=stack[-1]
                stack.pop()
                next=i
                if not stack:
                    prev=-1
                else:
                    prev=stack[-1]
                curr_area=heights[element]*(next-prev-1)
                max_area=max(curr_area,max_area)
            stack.append(i)
        while stack:
            next=len(heights)
            element=stack[-1]
            stack.pop()
            if not stack:
                prev=-1
            else:
                prev=stack[-1]

            curr_area=heights[element]*(next-prev-1)
            max_area=max(curr_area,max_area)
        return max_area