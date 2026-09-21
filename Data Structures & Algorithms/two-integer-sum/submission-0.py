class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash each value with its index

        hMap = {}

        for i in range(len(nums)):
            hMap[nums[i]] = i
        # {3:0, 4:1, ...}
    
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hMap and hMap[complement] != i:
                return [i, hMap[complement]]
