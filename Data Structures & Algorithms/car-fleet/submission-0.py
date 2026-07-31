class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]    
        st=[]
        stack=[]
        for i in range(0,len(position)):
            time.append((target-position[i])/speed[i])
        for i in range(len(position)):
            st.append((position[i],time[i]))
        st.sort()
        for i in range(len(st)-1,-1,-1):
            if stack and (st[i][1] > stack[-1]):
                stack.append(st[i][1])
            elif stack and (st[i][1] <= stack[-1]):
                continue
            else:
                stack.append(st[i][1])
        return len(stack)
        