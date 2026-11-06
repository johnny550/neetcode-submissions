from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]=count.get(n,0) +1
        for n,c in count.items():
            # number n appears c number of times
            freq[c].append(n)
        
        result=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result