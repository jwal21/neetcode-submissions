class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        '''
            - return the max volume of a container
            - the volume of a container is denoted by... 
            - the minimum of any two integers (heights) * the difference in index
            - e.g. heights = [1,7,2,5,4,7,3,6] -> min(7, 6) = 6 * (index of 6 - index of 7) = 6 * 6 = 36

            - we need to track index and value
            - 
        '''
        l, r = 0, len(heights) - 1
        maxVol = 0
        while l < r:
            currVol = min(heights[l], heights[r]) * (r - l)
            maxVol = max(maxVol, currVol)
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return maxVol




