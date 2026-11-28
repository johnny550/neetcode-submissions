class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> List[int]:
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


sol=Solution() 
print(sol.topKFrequent(["leetcode", "love", "coding", "i", "i", "love"], 2))
# ["i", "love"]

print(sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
# ["the", "is", "sunny", "day"]

print(sol.topKFrequent(["d", "c", "b", "a", "d", "c", "b", "a"],4))
# ["a", "b", "c", "d"]

print(sol.topKFrequent(["apple", "banana", "cherry", "apple", "banana", "date"],2))
# ["apple", "banana"]

print(sol.topKFrequent(["programming", "python", "algorithm","python", "programming", "python","leetcode", "algorithm"],3)
)
# ["python", "algorithm", "programming"]

print(sol.topKFrequent(["a", "b", "a"], 1))
# ["a", "b"]