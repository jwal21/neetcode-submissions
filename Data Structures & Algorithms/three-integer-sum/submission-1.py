class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ''' 
            - store triplets that sum to 0, as a list of lists
            - no duplicate triplets allowed
            - order of numbers does not matter
            - nums is not sorted

            - brute force approach would be to use 3 nested for loops to iterate through every possible combination
            - we could instead use a single for loop to iterate through the starting numbers
            - and then nest a while loop and perform a 2 pointer method on the sorted list nums

            e.g. 
                res = [] -> to store result triplets
                nums.sort() -> sort the list of nums to allow for 2 pointer method 
                
                for i in range(len(nums) - 1)
                    if nums[i] > 0:
                        break
                    l,r = ...

                    while l < r
                        temp 3sum, 
                        check if greater, less than or equal to 0
                        adjust pointers accordingly

                        if 3sum = 0, append nums to list
                            l =+ 1
                            r -= 1
                            if the previous left pointer is equal to the current left pointer AND left doesnt equal right:
                                l += 1
                return res
        
        '''

        res = []
        nums.sort()

        
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
        
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1 
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            















