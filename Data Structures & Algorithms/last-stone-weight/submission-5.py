class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        # access to the two heaviest stones
        # sorted list? to insert O(n) time
        # heap          insert in O(logn) time

        # store largest stones at heap[0] with maxHeap
        # initialize maxHeap

        maxHeap = []
        for i in stones:
            heapq.heappush_max(maxHeap, i)
        
        while len(maxHeap) > 1:

            y = heapq.heappop_max(maxHeap)
            x = heapq.heappop_max(maxHeap)
            if x == y:
                continue
            heapq.heappush_max(maxHeap, y - x)
        
        return maxHeap[0] if len(maxHeap) != 0 else 0



