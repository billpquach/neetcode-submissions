class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # calculate a price such that p = (right bound) - (left bound)
        # we want to choose the min
        # [10, 1, 0, 6, 7, 1]
        #        l      r   
        # move l pointer to index of r pointer only if p[r] < p[l]
        # price = p[r] - p[l]

        res = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            currPrice = prices[r] - prices[l]
            res = max(res, currPrice)
        return res

        
    
            


        