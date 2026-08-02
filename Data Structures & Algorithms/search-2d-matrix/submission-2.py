class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            left=0
            right=len(i)-1
            while left<=right:
                mid=(left+right)//2
                if target>i[mid]:
                    left=mid+1
                elif target<i[mid]:
                    right=mid-1
                elif target==i[mid]:
                    return True
        else:
            return False    