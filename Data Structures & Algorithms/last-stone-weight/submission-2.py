class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # the two heaviest stones
        # data structure to store an array of largest elems
        # maxHeap
        #   if y > x, where y = heapq.heappop(heap)
        #                   x = max(heap[0])

        #
        #   y = heapq.heappop(stones)
        #   x = heap[0]
        #   heapq.heappushpop(stones, y-x)

        #   y = 1
        #   x = 0
        #      0  
        #    
        heapq.heapify_max(stones)
        maxHeap = stones
        
        #print(maxHeap)
        for i in range(len(maxHeap)):
            #print(maxHeap)
            if len(maxHeap) <= 1:
                break
            
            y = heapq.heappop_max(maxHeap)
            # alternatively
            # x = heapq.heappop_max(maxHeap)
            x = maxHeap[0]
            heapq.heappop_max(maxHeap)
            heapq.heappush_max(maxHeap, y-x)
        #print(maxHeap)
        return maxHeap[0]