class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        heap = []

        for key in count:
            if len(heap) < k or count[key] > heap[0][0]:
                heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])
        return res