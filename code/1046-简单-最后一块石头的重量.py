import heapq

def lastStoneWeight(tones):
    heap_stones = [-i for i in stones]
    heapq.heapify(heap_stones)
    while len(heap_stones) > 1:
        x = heapq.heappop(heap_stones)
        y = heapq.heappop(heap_stones)
        if x==y:
            continue
        else:
            heapq.heappush(heap_stones, -abs(x-y))
    if len(heap_stones)==0:
        return 0
    else:
        return -heap_stones[0]