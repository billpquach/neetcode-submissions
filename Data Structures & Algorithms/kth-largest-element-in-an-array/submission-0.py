class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k-th largest 
        # keep an array of size k and return the minimum if nums[i] > min[0]
        # ex, k = 2, nums = [2,3,1,5,4]
        # minHeap = [4,5]       -->> minHeap solution
        minHeap = []

        for i in range(len(nums)):

            if len(minHeap) < k or nums[i] > minHeap[0]:
                heapq.heappush(minHeap, nums[i])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
        

