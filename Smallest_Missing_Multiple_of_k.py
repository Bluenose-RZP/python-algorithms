'''Given an integer array numbs and an integer k, return the smallest positive multiple of k that is missing from numbs.
a multiple of k is any positive integer divisible by k.
example 1:
input nums = [8,2,3,4,6] k = 2
Output: 10
This one was relatively easy for me and just took the one iteration. Time and space complexity are both O(n).
'''
'''
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        checkList = {}
        mNum = 1
        for number in nums:
            checkList[number] = True
        while True:
            if not checkList.get(k * mNum):
                return (k * mNum)
            mNum += 1

'''
# I realized that using a set would be better than an empty dictionary and remade it for practice.
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numSet = set(nums)
        mNum = 1
        while True:
            if (k * mNum) not in numSet:
                return (k * mNum)
            mNum += 1
