class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        l, r  = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                print('leftMax = ', leftMax)
                res += leftMax - height[l]
                print('current res = ', res)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                print('rightMax = ', rightMax)
                res += rightMax - height[r]
                print('current res = ', res)
        return res