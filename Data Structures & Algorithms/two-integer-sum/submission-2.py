class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash each value with its index
        # target - nums[i] = complement, the other element in nums we 
        # want to find
        # if complement in hMap, reference its index and return both indices

        hMap = {}

        for i in range(len(nums)):
            hMap[nums[i]] = i
            # {3: 0, 4: 1, 5: 2, 6: 3} with O(1) lookup
        

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hMap and hMap[complement] != i:
                return [i, hMap[complement]]
            

