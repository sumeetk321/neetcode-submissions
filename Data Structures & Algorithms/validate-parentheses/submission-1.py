class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if stack:
                if s[i]==')' and stack[len(stack)-1]=='(':
                    stack.pop()
                    continue
                if s[i]==']' and stack[len(stack)-1]=='[':
                    stack.pop()
                    continue
                if s[i]=='}' and stack[len(stack)-1]=='{':
                    stack.pop()
                    continue
            if s[i]=='(' or s[i]==')' or s[i]=='[' or s[i]==']' or s[i]=='{' or s[i]=='}':
                stack.append(s[i])
        #print(stack)
        return len(stack)==0