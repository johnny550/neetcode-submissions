class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # maintain the window length
        # permutations have the same length as original substring
        # order of letters does not matter
        # frequency of letters does
        sorted_s1=sorted(s1)
        p1,p2=0,len(sorted_s1)
        l_s2=list(s2)
        while p2<=len(s2):
            combo=l_s2[p1:p2]
            if sorted(combo)==sorted_s1:
                return True
            p1+=1
            p2+=1
        return False