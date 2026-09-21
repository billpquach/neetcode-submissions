class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)

        l_prod, r_prod = 1, 1

        for i in range(len(nums)):
            l_arr[i] = l_prod
            l_prod *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            r_arr[i] = r_prod
            r_prod *= nums[i]

        for i in range(len(nums)):
            r_arr[i] *= l_arr[i]

        return r_arr