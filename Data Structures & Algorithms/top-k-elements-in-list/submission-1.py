from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        return sorted(freq, key=lambda x:-freq[x])[:k]

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

print(sol.topKFrequent(["a", "b", "a"], 5))
# ["a", "b"]