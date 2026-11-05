import heapq

## get min from set of values indefinitely
# with minheaps min val will always be at index 0
min_heap=[]
heapq.heappush(min_heap,10)
heapq.heappush(min_heap,4)
heapq.heappush(min_heap,5)

print("Before popping", min_heap)
while len(min_heap):
    print(heapq.heappop(min_heap))
print("After popping", min_heap)

## get max from set of values indefinitely
# with maxheaps max val will always be at index 0
# no max heap in python by default.
# workaround: same logic as minheap but multiply by -1 when pushing & popping
max_heap=[]
# heapq.heappush(max_heap, -1 * 10)
# heapq.heappush(max_heap, -1 * 4)
# heapq.heappush(max_heap, -1 * 5)
heapq.heappush_max(max_heap,  10)
heapq.heappush_max(max_heap,  4)
heapq.heappush_max(max_heap, 5)

print("Before popping", max_heap)
while len(max_heap):
    print(heapq.heappop(max_heap) * -1)
print("After popping", max_heap)