class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            #print(l, r)
            mid = l + (r-l)//2
            #print(mid)
            if nums[r] >= nums[mid]:
                r = mid
            else:
                l = mid+1
        if l==len(nums):
            return nums[0]
        else:
            return nums[l]


