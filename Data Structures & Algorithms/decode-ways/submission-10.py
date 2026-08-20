class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0]=='0':
            return 0
        if len(s) < 2:
            return 1
        arr = [0] * len(s)

        if s[-1]!='0':
            arr[-1] = 1
        if int(s[-2])!=0:
            if int(s[-2]+s[-1]) <= 26:
                arr[-2] = arr[-1]+1
            else:
                arr[-2] = arr[-1]
        for i in range(len(s)-3, -1, -1):
            if s[i]=='0':
                arr[i] = 0
            elif int(s[i]+s[i+1]) <= 26:
                arr[i] = arr[i+1]+arr[i+2]
            else:
                arr[i] = arr[i+1]
        return arr[0]