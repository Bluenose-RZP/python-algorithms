'''This one took a few minutes of thinking to figure out a decent O(n) solution, but wasn't too hard.
Still, my runtime and runspace were both below average.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sList = {}
        tList = {}
        for char in s:
            sList.setdefault(char, 0)
            sList[char] = sList[char] + 1
        for char in t:
            tList.setdefault(char, 0)
            tList[char] = tList[char] + 1
        if sList == tList:
            return True
        return False
  '''
'''This second solution is a bit more efficient. It uses a single pass instead of two, cutting the space used and very slightly improving the speed.
Also charCheck.get(char, 0) + 1 is a bit faster I believe than the two lines setdefault and then += 1
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCheck = {}
        for char in s:
            charCheck[char] = charCheck.get(char, 0) + 1
        for char in t:
            if char not in charCheck:
                return False
            charCheck[char] = charCheck[char] - 1
            if charCheck[char] == 0:
                del charCheck[char]
        return True
