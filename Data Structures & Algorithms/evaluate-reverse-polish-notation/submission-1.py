class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t=="+" or t=="-" or t=="*" or t=="/":
                o1 = stack.pop()
                o2 = stack.pop()
                #print(o1, o2)
                if t=="+":
                    stack.append(o1+o2)
                    #print(stack)
                elif t=="-":
                    stack.append(o2-o1)
                elif t=="*":
                    stack.append(o1*o2)
                elif t=="/":
                    stack.append(int(o2/o1))
            else:
                stack.append(int(t))
        return stack[0]
