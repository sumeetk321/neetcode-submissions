class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            g = 0
            for j in range(i, i+len(gas)+1):
                g+=gas[j%len(gas)]-cost[j%len(gas)]
                if g < 0:
                    break
            if j==i+len(gas):
                return i%len(gas)
        return -1