'''def twoSum(nums, target): #This is a 0(n^2) brute force solution that I believe works
    numtest = 0
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            print(f'x is {x} and y is {y}')
            numtest = nums[x] + nums[y]
            print(numtest)
            if numtest == target:
                return [x, y]
'''

'''def twoSum(nums, target): # my initial dictionary solution
    numList = {}
    num1 = 0
    num2 = 0
    for i in range(len(nums)):
        if nums[i] in numList:
            if nums[i] * 2 == target:
                return (numList[nums[i]], i)
        numList[nums[i]] = i
    # print(numList)
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        if num2 in numList and num2 != num1:
            return [i, numList[num2]]
'''

def twoSum(nums, target):
    numList = {}
    for i in range(len(nums)):
        num1 = target - nums[i]
        if num1 in numList:
            return [numList[num1], i]
        else:
            numList[nums[i]] = i

           
sample1 = [2,7,11,15]
sample2 = [3,2,4]
sample3 = [3,3]
print(twoSum(sample1, 9))
print(twoSum(sample2, 6))
print(twoSum(sample3, 6))
