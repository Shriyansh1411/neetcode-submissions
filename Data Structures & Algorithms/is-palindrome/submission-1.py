class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        ch=0
        for i in s:
            if (i.isalnum()):
                t+=i
        
        t=t.lower()
        right=len(t)-1
        left=0

        while (left<right):
     
            if (t[left]!=t[right]):
                ch=1
                break
            else:
                right-=1
                left+=1
        if ch==1:
            return False 
        else:
            return True
            