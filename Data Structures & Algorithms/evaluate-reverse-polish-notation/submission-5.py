class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char not in ['+','-','*','/']:
                stack.append(int (char))
            else:
                rightop=int(stack.pop())
                leftop=int(stack.pop())
                if char=="+":
                    conversion= leftop + rightop
                    stack.append(conversion)
                if char=="-":
                    conversion= leftop - rightop
                    stack.append(conversion)
                if char=="*":
                    conversion= leftop * rightop
                    stack.append(conversion)
                if char=="/":
                    conversion= int (leftop / rightop)
                    stack.append(conversion)
        return stack[-1]