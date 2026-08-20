class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        l = len(nums)
        for n in nums:
            s+=n
        return abs(s-((l+1)*l)//2)
        