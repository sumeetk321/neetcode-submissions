class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        for p, s in sorted(zip(position, speed), key = lambda x : x[1]):
            print(stack)
            if len(stack)==0:
                stack.append((p,s))
                continue
            add = True
            for p1, s1 in stack:
                if p==p1:
                    add = False
                    break
                if s1!=s:
                    timemeet = ((p-p1)/(s1-s))
                    meet = s*timemeet+p
                    print(p, s, p1, s1, timemeet, meet)
                    if timemeet >= 0 and meet >= max(p, p1) and meet <= target:
                        add = False
                        break
            
            if add:
                stack.append((p,s))
        print(stack)
        return len(stack)
                
                