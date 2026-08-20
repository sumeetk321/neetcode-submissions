import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l<r:
            mid = l+(r-l)//2
            #print(l, r)
            s = 0
            for p in piles:
                s+=math.ceil(p/mid)
            if s<=h:
                r = mid
            else:
                l = mid+1
        
        return l