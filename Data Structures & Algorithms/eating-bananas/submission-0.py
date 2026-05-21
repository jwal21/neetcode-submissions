class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h is the time limit for eating all piles of bananas. is always >= length of piles
        # if a pile is eaten before an hour is up, you still have to wait the whole hour until the next
        
        l, r = 1, max(piles)
        
        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

        


