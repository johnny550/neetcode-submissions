class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        known_letters_s={}
        known_letters_t={}
        for i in range(len(s)):
            known_letters_s[s[i]]=1+known_letters_s.get(s[i],0)
            known_letters_t[t[i]]=1+known_letters_t.get(t[i],0)
        
        
        return known_letters_s==known_letters_t