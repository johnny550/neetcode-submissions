import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip s of all nonalphaN chars
        triage_letters=[]
        for letter in list(s):
            if letter in string.ascii_lowercase or letter in  string.ascii_uppercase or letter in  string.digits:
                # case insensitiveness
                triage_letters+=letter.lower()
        
        # place a pointer at each end of the substring
        p2=len(triage_letters)-1
        for p1,l1 in enumerate(triage_letters):
            # if at any time pointers show different letters: return false
            # return true
            if l1!=triage_letters[p2]:
                return False
            p2-=1
        return True
        