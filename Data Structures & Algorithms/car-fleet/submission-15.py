class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        for p, s in sorted(zip(position, speed), key = lambda x : x[1]):
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
                    if timemeet >= 0 and meet >= max(p, p1) and meet <= target:
                        add = False
                        break
            
            if add:
                stack.append((p,s))
        return len(stack)
                
                