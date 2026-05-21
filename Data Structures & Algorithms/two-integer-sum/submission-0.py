class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] 
        return []

        

        """
        compliment = 0
        for num in nums:
            compliment = target - num
            if compliment in nums:
                return [num, nums[compliment]]
        return False
        """
        
