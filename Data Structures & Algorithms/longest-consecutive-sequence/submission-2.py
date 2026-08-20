class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        res = 0
        while m:
            curr = m.pop()
            currLongest = 1
            tmp = curr
            while tmp-1 in m:
                m.remove(tmp-1)
                currLongest += 1
                tmp -= 1
            tmp = curr
            while tmp+1 in m:
                m.remove(tmp+1)
                currLongest += 1
                tmp += 1
            res = max(res, currLongest)
        return res