class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        known_letters_s={}
        known_letters_t={}
        for i in range(len(s)):
            known_letters_s[s[i]]=1+known_letters_s.get(s[i],0)
            known_letters_t[t[i]]=1+known_letters_t.get(t[i],0)
        # for i in s:
        #     if i not in known_letters_s:
        #         known_letters_s[i]=1
        #     else:
        #         known_letters_s[i]+=1
        # for i in t:
        #     if i not in known_letters_t:
        #         known_letters_t[i]=1
        #     else:
        #         known_letters_t[i]+=1
        
        
        return known_letters_s==known_letters_t