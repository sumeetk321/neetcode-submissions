class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        m = 0
        while r>l:
            m = max(m, (r-l)*min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return m