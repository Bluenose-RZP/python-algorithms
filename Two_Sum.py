def twoSum(nums, target): # Checks which two numbers in a list(nums) equal (target)
    numList = {} #create a dictionary
    for i in range(len(nums)): #push the list into the dictionary, checking for solution
        num1 = target - nums[i]
        if num1 in numList:
            return [numList[num1], i]
        else:
            numList[nums[i]] = i
