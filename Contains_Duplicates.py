'''This one was quick and easy. The Dictionary makes it O(n) time and space overall. After working hard on other problems
I was surprised at how quick and simple it was.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkList = {}
        for num in nums:
            if checkList.get(num):
                return True
            else:
                checkList[num] = True
        return False
