class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            target = -nums[i]
            while r>l and r!=i and l!=i:
                if nums[l]+nums[r]==target:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l+=1
                elif nums[l]+nums[r] < target:
                    l+=1
                elif nums[l]+nums[r] > target:
                    r-=1
        return res