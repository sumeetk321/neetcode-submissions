class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False for i in range(len(s))]
        for e in range(len(s)-1, -1, -1):
            
            for word in wordDict:
                
                if e+len(word) <= len(s):
                    check = s[e:e+len(word)]
                    print(check)
                    if check==word:
                        print("IN HERE", e, word)
                        if e+len(word)==len(s):
                            arr[e] = True
                        else:
                            arr[e] |= arr[e+len(word)]
        print(arr)
        return arr[0]