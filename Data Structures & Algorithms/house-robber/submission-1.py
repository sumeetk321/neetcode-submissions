class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        arr = [0 for i in range(len(nums))]
        arr[-1] = nums[-1]
        arr[-2] = nums[-2]
        for i in range(len(nums)-3, -1, -1):
            arr[i] = max(nums[i]+arr[i+2], arr[i+1])
        return arr[0]