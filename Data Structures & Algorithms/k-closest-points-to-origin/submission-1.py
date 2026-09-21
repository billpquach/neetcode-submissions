class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Data structure?
        # closest == smallest distance
        # we want to keep track of the smallest k coords
        # in an array...
        # therefore we want a minHeap of tuples (dist, coord)
        def calcDistance(x, y):
            distance = math.sqrt((x)**2 + (y)**2)
            return distance
        maxHeap = []

        for i in range(len(points)):
            currDistance = calcDistance(points[i][0],points[i][1])
            
            if len(maxHeap) < k or currDistance < maxHeap[0][0]:
                heapq.heappush_max(maxHeap, (currDistance, points[i]))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
            #print(maxHeap)
        res = []
        for i in range(len(maxHeap)):
            res.append(maxHeap[i][1])
        return res

        """

        (2, [0,2])
(2.67,[2,2])


        """



        