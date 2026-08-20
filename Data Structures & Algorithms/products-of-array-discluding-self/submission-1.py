class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroprod = 1
        zeroseen = False
        for i in range(len(nums)):
            prod*=nums[i]
            if nums[i] == 0 and not zeroseen:
                zeroseen = True
            elif nums[i]==0 and zeroseen:
                zeroprod = 0
            elif nums[i]!=0:
                zeroprod*=nums[i]
        out = []
        for i in range(len(nums)):
            if nums[i] != 0:
                out.append(int(prod/nums[i]))
            else:
                out.append(zeroprod)
        return out