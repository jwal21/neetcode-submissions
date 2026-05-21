class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # list to store sublists (triplets)
        res = []
        # sorting the nums list
        nums.sort()

        # enumerate through nums
        for i, v in enumerate(nums):
            # if num is > 0- this means the sum of any three cannot equal 0 (as nums is now sorted)
            if v > 0:
                break
            # if current index is not the first (0) and the previous number is equal to the current number- continue 
            if i > 0 and v == nums[i - 1]:
                continue
            
            # set left pointer to be adjacent index to current index and right pointer to be the last index
            l, r = i + 1, len(nums) - 1
            while l < r:
                # setting current three-sum
                threeSum = v + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1 
                elif threeSum > 0:
                    r -= 1
                else:
                    # append valid threesome to result
                    res.append([v, nums[l], nums[r]])
                    # shift pointers left and right
                    l += 1
                    r -= 1
                    
                    # if the current left pointer value is equal to the value before it (would result in duplicate triplets)
                    # AND left isnt equal to right -> shift left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
