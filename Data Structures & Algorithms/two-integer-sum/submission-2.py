class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = defaultdict(int)
        for i in range(len(nums)):
            m[nums[i]] = i

        res = []

        for i in range(len(nums)):
            if target-nums[i] in nums and m[target-nums[i]] != i:
                return [i, m[target-nums[i]]]