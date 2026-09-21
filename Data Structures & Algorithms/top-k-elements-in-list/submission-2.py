class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to count the instances of each num
        # utilize a heapq to only keep track of the k most frequent
        # that is, len(heapq) == k

        counter = Counter(nums)
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [num for count, num in heap]