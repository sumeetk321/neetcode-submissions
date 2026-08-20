class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        arr = [[] for m in range(len(nums)+1)]
        for n in nums:
            d[n] = d.get(n, 0)+1
        
        for key in d.keys():
            arr[d[key]].append(key)
        
        i = 0
        idx = len(nums)
        res = []
        #print(arr)
        while i < k and idx>0:
            if len(arr[idx]) > 0:
                res+=(arr[idx])
                i+=len(arr[idx])
            idx-=1

        return res