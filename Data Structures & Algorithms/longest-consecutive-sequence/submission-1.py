class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for val in s:
            if val-1 not in s:
                l = 1
                tmp = val
                while tmp+1 in s:
                    l+=1
                    tmp+=1
                res = max(res, l)
        return res                