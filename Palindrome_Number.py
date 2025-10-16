from math import log10, floor

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
             return True 
        if x < 0:
             return False
        xLen = floor(log10(x)) + 1
        if xLen == 1:
             return True
        #odd = 1 if x % 2 else 0 # sets odd to 1 if odd
        for i in range(xLen // 2):
            first = (x // (10**(xLen - i - 1))) % 10 #front number
            second = (x // (10**(i))) % 10 # trailing number
            if first != second:
                return False
        return True
