class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        
        for index,letter in known_letters_t.items():
            print(known_letters_t)
            return known_letters_s==known_letters_t