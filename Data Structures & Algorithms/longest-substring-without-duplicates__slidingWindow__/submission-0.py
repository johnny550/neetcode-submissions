class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        maxLength,p1=0,0
        for p2 in range(len(s)):
            while s[p2] in charSet:
                charSet.remove(s[p1])
                p1+=1
            charSet.add(s[p2])
            maxLength=max(maxLength,p2-p1+1)

        return maxLength