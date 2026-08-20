class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)<=2:
            return max(nums)
        def dp(n):
            arr = [0]*len(n)
            arr[0] = n[0]
            arr[1] = max(n[0],n[1])
            for i in range(2, len(n)):
                arr[i] = max(arr[i-1], n[i]+arr[i-2])

            print(n, arr)
            return arr[-1]

        print(dp(nums[:-1]))
        print(dp(nums[1:]))
        return max(dp(nums[:-1]), dp(nums[1:]))
            