class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1]+=1
            return digits
        i = len(digits)-1

        rem = 0
        while i >= 0 and digits[i]==9:
            digits[i] = 0
            rem+=1
            i-=1
        if i < 0:
            digits.insert(0, 1)
            return digits
        else:
            digits[i]+=1
            return digits
        