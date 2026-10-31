class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to count the instances of each num
        # utilize a heapq to only keep track of the k most frequent
        # that is, len(heapq) == k

        count = Counter(nums)
        # [1, 1, 1, 2 ,2, 2, 2, 2, 3, 3]
        # {1: 3, 2: 5, 3: 2, 6: 7}
        # {7: 2}
        
        # maxHeap or minHeap?
        # minHeap

        #       (5, 2)
        #    (7: 6)
        #

        heap = []
        for key in count:
            if len(heap) < k or count[key] > heap[0][0]:       # value       key
                # using a tuple helps keep key value pairs
                heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in heap:
            res.append(i[1])
        return res