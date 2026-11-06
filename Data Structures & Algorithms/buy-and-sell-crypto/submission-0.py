class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # calculate a price such that p = (right bound) - (left bound)
        # we want to choose the min
        # [10, 1, 0, 6, 7, 1]
        #        l      r   
        # move l pointer to index of r pointer only if p[r] < p[l]
        # price = p[r] - p[l]

        l = 0
        res = 0
        if len(prices) == 1:
            return 0
        # res = 6
        for r in range(1, len(prices)):

            curr_price = prices[r] - prices[l]
            res = max(res, curr_price)
            if prices[r] < prices[l]:
                l = r
        return res
            


        