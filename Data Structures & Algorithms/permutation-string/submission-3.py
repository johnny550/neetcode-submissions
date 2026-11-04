class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # maintain the window length
        # permutations have the same length as original substring
        # order of letters does not matter
        # frequency of letters does
        p1,p2=0,len(s1)
        l_s2=list(s2)
        s1_hm=Counter(s1)
        while p2<=len(s2):
            combo=l_s2[p1:p2]
            combo_hm=Counter(combo)
            if combo_hm==s1_hm:
                return True
            p1+=1
            p2+=1
        return False