import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        triage_letters=[]
        for l in s:
            if l.isalnum():
                # case insensitiveness
                triage_letters+=l.lower()
        return triage_letters==triage_letters[::-1]