class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hMap = {}
        for i in range(len(nums)):
            hMap[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hMap and hMap[complement] != i:
                return [i, hMap[complement]]
            