from collections import Counter
import heapq

def top_k_frequent(words: list[str], k: int) -> list[str]:
    # 1- count each word
    # 2- keep data in dict where k=word and v=count
    # Iteration 1
    # word_count={}word_count=Counter(words)
    # for w in words:
    #     try:
    #         word_count[w]=word_count[w]+1
    #     except KeyError:
    #         word_count[w]=1
    # # 3- make a derivative list of keys sorted by count from dict
    # sorted_keys_by_count=sorted(word_count, key=lambda w: (-word_count[w], w))
    # # 4- return the k elements
    # print(sorted_keys_by_count[:k])
    
    # Iteration 2: 
    # 1- word count as dict
    # word_count=Counter(words)
    # # 2- sort keys by count and cut the slice needed
    # most_frequent_words=sorted(word_count, key=lambda w:(-word_count[w],w))[:k]
    
    # key=lambda w: (-counts[w], w)
    # lambda w: is a throwaway function that takes a word w.
    # It returns a tuple: (-counts[w], w).
    # Python calls it once per word and sorts by the returned tuples, not the words themselves.

    # More about (-counts[w], w)
    # -count: frequency
    # w: if elements are tied, sort by alpabetical order
    # Say "i" and "love" both have count 2:
    # (-2, "i")  vs  (-2, "love")
    # First elements are equal, so Python compares "i" < "love" → True, and "i" comes first.
    
    # Iteration 3
    # no need to sort all m unique words when k is much smaller than m
    word_count=Counter(words)
    most_frequent_words=heapq.nlargest(k, word_count, key=lambda w:(word_count[w],w))
    
    print(most_frequent_words)
    
    
    
    
top_k_frequent(["leetcode", "love", "coding", "i", "i", "love"], 2)
# ["i", "love"]

top_k_frequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
# ["the", "is", "sunny", "day"]

top_k_frequent(["d", "c", "b", "a", "d", "c", "b", "a"],4)
# ["a", "b", "c", "d"]

top_k_frequent(["apple", "banana", "cherry", "apple", "banana", "date"],2)
# ["apple", "banana"]

top_k_frequent(["programming", "python", "algorithm","python", "programming", "python","leetcode", "algorithm"],3)
# ["python", "algorithm", "programming"]

top_k_frequent(["a", "b", "a"], 5)
# ["a", "b"]