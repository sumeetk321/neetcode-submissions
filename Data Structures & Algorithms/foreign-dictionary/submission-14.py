class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        charSet = set()
        for word in words:
            charSet.update(word)
        adjList = {c:[] for c in charSet}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            j = 0
            while j < len(w1) and j < len(w2) and w1[j]==w2[j]:
                j+=1
            if j>=len(w2):
                if j < len(w1):
                    return ""
                continue
            if j >= len(w1):
                continue
            if w1[j] not in adjList[w2[j]]:
                adjList[w2[j]].append(w1[j])
        def topsort(adjList):
            no_dependencies = []
            for c in adjList:
                if len(adjList[c])==0:
                    no_dependencies.append(c)
            
            result = []

            while no_dependencies:
                curr = no_dependencies.pop()
                result.append(curr)

                for c in adjList:
                    if curr in adjList[c]:
                        adjList[c].remove(curr)
                        if len(adjList[c])==0:
                            no_dependencies.append(c)
            
            if len(result)==len(adjList):
                return result
            return []
        
        return ''.join(topsort(adjList))

                
            
