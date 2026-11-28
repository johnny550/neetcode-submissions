from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # maintain the window length
        # permutations have the same length as original substring
        # order of letters does not matter
        # frequency of letters does
        l,r=0,len(s1)-1
        base_perm=Counter(s1)
        while r<len(s2):
            possible_permutation=s2[l:r+1]
            x=Counter(possible_permutation)
            if base_perm==x:
                return True
            else:
                l,r=l+1,r+1       
        return False