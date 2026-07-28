class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            elif ( i==')' or i=="]" or i=="}" ) and len(stack)>0:
                element=stack.pop()
                if element=='(' and i==')':
                    continue
                if element=='[' and i==']':
                    continue
                if element=='{' and i=='}':
                    continue
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
        