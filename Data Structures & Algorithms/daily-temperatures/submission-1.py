class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        i=0
        j=1
        while j<len(temperatures):
            if temperatures[j]>temperatures[i]:
                stack.append(j-i)
                i+=1
                j=i+1
            elif (j==len(temperatures)-1 and temperatures[i]>temperatures[j]) or j>=len(temperatures)-1:
                stack.append(0)
                i+=1
                j=i+1
            else:
                j+=1
        else:
            stack.append(0)
        return stack 