class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)] 
        m = Counter(nums)
        for n in m.keys():
            buckets[m[n]].append(n)
        rem = k
        idx = len(nums)-1
        res = []
        while rem > 0:
            while buckets[idx] and rem > 0:
                res.append(buckets[idx].pop())
                rem -= 1
            idx -= 1
        return res

