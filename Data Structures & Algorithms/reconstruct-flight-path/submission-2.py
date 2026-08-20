import bisect
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = {}
        for f, t in tickets:
            if f not in adjList.keys():
                adjList[f] = []
            if t not in adjList.keys():
                adjList[t] = []
            adjList[f].append(t)

        for k in adjList.keys():
            adjList[k].sort()
            adjList[k] = collections.deque(adjList[k])
        
        #print(adjList)
        res = []
        out = []
        numAirports = len(adjList.keys())
        def dfs(node):
            nonlocal out
            #print(node, res)
            if len(out) > 0:
                return True
            if len(adjList[node])==0 and len(res)==len(tickets) and len(out)==0:
                res.append(node)
                out = res
                return True
            
            i = 0
            for neighbor in adjList[node].copy():
                adjList[node].remove(neighbor)
                res.append(node)
                if dfs(neighbor):
                    return True
                res.pop()
                bisect.insort(adjList[node], neighbor)
            return False
        
        dfs("JFK")
        return out
        

