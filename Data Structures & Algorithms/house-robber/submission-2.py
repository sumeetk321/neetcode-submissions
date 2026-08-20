class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        tmp1 = nums[-1]
        tmp2 = nums[-2]
        for i in range(len(nums)-3, -1, -1):
            tmp3 = tmp2
            tmp2 = max(nums[i]+tmp1, tmp2)
            tmp1=tmp3
        return tmp2