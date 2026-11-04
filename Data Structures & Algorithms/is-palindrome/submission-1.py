import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1,p2=0,len(s)-1
        lower_s=s.lower()
        while p1<p2:
            while p1<p2 and not self.isAlphaNum(lower_s[p1]):
                p1+=1
            while p2>p1 and not self.isAlphaNum(lower_s[p2]):
                p2-=1
            if lower_s[p1]!=lower_s[p2]:
                print(lower_s[p1],lower_s[p2])
                return False
            p1,p2=p1+1,p2-1
        return True

    def isAlphaNum(self, c)->bool:
        return (ord(c) in range(97,122) or ord(c) in range(48,57))
        # if ord(c) in range(97,122) or ord(c) in range(48,57):
        #     print(f"letter: {c}, ascii:{ord(c)}")
        #     return True
        # return False 