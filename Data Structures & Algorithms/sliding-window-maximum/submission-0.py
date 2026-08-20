class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        count = dict()
        for i in range(k):
            count[nums[i]] = count.get(nums[i], 0)+1
        res = [max(count.keys())]
        while r < len(nums)-1:
            count[nums[l]]-=1
            if count[nums[l]]==0:
                del count[nums[l]]
            l+=1
            r+=1
            count[nums[r]] = count.get(nums[r], 0)+1
            res.append(max(count.keys()))
        return res