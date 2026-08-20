class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        if l==0:
            l = len(nums)-1
        else:
            l -= 1

        print(l)
        l1 = 0
        r1 = len(nums)-1
        if target > nums[0] and target < nums[l]:
            r1 = l
        elif target < nums[0]:
            l1 = l+1
        while l1<r1:
            mid = l1+(r1-l1)//2
            if nums[mid] >= target:
                r1 = mid
            else:
                l1 = mid+1
        print(l1)
        if l1 < 0 or l1 >= len(nums):
            return -1
        if nums[l1]==target:
            return l1
        return -1
            
