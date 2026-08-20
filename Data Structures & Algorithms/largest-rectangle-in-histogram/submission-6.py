class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        end = len(heights)
        stack = []
        res = 0
        for i, h in enumerate(heights):
            if len(stack)==0:
                stack.append((i, h))
                continue
            itmp = i
            while len(stack) > 0 and stack[-1][1] > h:
                newval = (i-stack[-1][0])*stack[-1][1]
                res = max(res, newval)
                itmp = min(itmp, stack[-1][0])
                stack.pop()
            
            stack.append((itmp, h))

        while len(stack) > 0:
                newval = (end-stack[-1][0])*stack[-1][1]
                res = max(res, newval)
                stack.pop()
        return res
            
