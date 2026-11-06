class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        known_letters_s={}
        known_letters_t={}
        for i in s:
            if i not in known_letters_s:
                known_letters_s[i]=1
            else:
                known_letters_s[i]+=1
        for i in t:
            if i not in known_letters_t:
                known_letters_t[i]=1
            else:
                known_letters_t[i]+=1
        
        
        return known_letters_s==known_letters_t