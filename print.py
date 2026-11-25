tab=[0,3,4]
print(2 * tab[-1])
# REVERSE
l=[0,1,2,3]
print(l[:-1])

# LAST ELEMENT
l=[0,1,3]
print(f"last el {l[-2]}")

num=-2
print(isinstance(num, int))
# A LIST B MADE OF AS MANY LISTS AS A LIST A CONTAINS NUMBERS
base_list=[1,2,3,4,5]
# l=[[]  for i in range(len(base_list))]
print(f"list B: {l}")

# everything reversed
l=[2,3,1,4,5]
print(l[::-1])
for i in range(len(l),0,-1):
    print(f"reverted: {i}")
print(sorted(l,reverse=True))

import heapq
print(f"original list {l}")
heapq.heapify_max(l)
print(f"heapified list {l}")