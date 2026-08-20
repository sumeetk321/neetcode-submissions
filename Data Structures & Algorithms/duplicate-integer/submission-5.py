class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        c = Counter(nums)
        return max(c.values()) > 1