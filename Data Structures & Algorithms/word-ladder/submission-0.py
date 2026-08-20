class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def oneAway(w1, w2):
            diff = False
            for i in range(len(w1)):
                if w1[i]!=w2[i]:
                    if diff:
                        return False
                    else:
                        diff = True
            return diff
        wordList.append(beginWord)
        adjList = {word:[] for word in wordList}
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if oneAway(wordList[i], wordList[j]):
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])
        print(adjList)
        visited = set()
        def bfs(word):
            q = collections.deque()
            q.append((1, word))
            while q:
                dist, popword = q.popleft()
                if popword in visited:
                    continue
                print(dist, popword)
                visited.add(popword)
                if popword==endWord:
                    return dist
                q.extend((dist+1, n) for n in adjList[popword])
            return 0
        return bfs(beginWord)

