class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inc = True
        for i in range(len(digits)-1,-1,-1):
            if inc:
                new = digits[i] +1
                digits[i] = new % 10
            else:
                break
            if new // 10 >= 1:
                inc = True
            else: 
                inc = False 
            
        if inc:
            return [1] + digits
        else:
            return digits