class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       hashMap = {}

       for index, val in enumerate(nums):
            compliment = target - val
            if compliment in hashMap:
                return [hashMap[compliment], index]
            hashMap[val] = index
        
    
        
