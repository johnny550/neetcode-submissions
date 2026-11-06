l=[0,1,2,3]
print(l[:-1])

l=[0,1]
print(l[-1])

base_list=[1,2,3,4,5]
l=[[]  for i in range(len(base_list))]
print(l)

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