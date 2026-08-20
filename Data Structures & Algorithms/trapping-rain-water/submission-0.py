class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        lbar, rbar = height[l], height[r]
        while l<r:
            if lbar < rbar:
                l+=1
                lbar = max(lbar, height[l])
                res+=lbar-height[l]
            else:
                r-=1
                rbar = max(rbar, height[r])
                res+=rbar-height[r]
        return res