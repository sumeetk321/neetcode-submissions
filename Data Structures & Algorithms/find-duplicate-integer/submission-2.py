class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while slow < len(nums) and fast < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        n = 0
        while nums[n]!=nums[slow]:
            slow = nums[slow]
            n = nums[n]

        return nums[slow]