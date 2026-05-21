class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # at each point, we need the product of the left most elements * product of right most elements
        
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
