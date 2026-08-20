class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        ma = [0]*len(nums)
        mi = [0]*len(nums)

        ma[0] = nums[0]
        mi[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                ma[i] = max(nums[i], mi[i-1]*nums[i])
                mi[i] = min(nums[i], ma[i-1]*nums[i])
            else:
                ma[i] = max(nums[i], ma[i-1]*nums[i])
                mi[i] = min(nums[i], mi[i-1]*nums[i])

        print(mi, ma)
        return max(ma)
