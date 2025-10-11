'''Reverse Integer:

Given a signed 32-bit integer x, return x with it's digits reversed.
if reversing causes the value to go outside the signed 32-bit integer range:
[-2^31, 2^31 - 1] then return 0 (-2147483648, 2147483647).
Example 1: input x = 123 ---- Output 321
Example 2: input x = -123 ---- OUtput -321
Example 3: input x = 120 ---- output 21'''

# 123000 = 000321 = 321
'''This first try is a string manipulation and solves the problem, but slower
than it could with a convoluted check that avoids creating a large int
in a way unnecessary in python, because python auto converts int numbers
larger than 32-bit to a larger, functional number. Also my check works, but
confused grok even when justified. 
'''
'''def reverse(x: int) -> int: 
    if x == 0:
        return 0
    numStr = str(abs(x)) # numStr is a string of the input made positive
    numStr = numStr.rstrip('0') # I originally forgot i needed to assign numStr
    numList = []
    for char in numStr:
        numList.insert(0, char)
    numStrReverse = ''.join(numList)
    if len(numStrReverse) == 10:
        if int(numStrReverse[0]) > 2:
            return 0
        elif int(numStrReverse[0]) == 2:
            numCheck = int(numStrReverse[1:])
            if x > 0:
                numCheck += 1
            if numCheck > 147483648:
                return 0
    answer = int(numStrReverse)
    if x > 0:
        return answer
    else:
        return answer * (-1)
'''

'''My new attempt, replaces the inefficient list reversal with a simple slice,
negatively iterated through the string to reverse it. it also takes advantage
of python's advanced int understanding to completely avoid my string evaluation
and just simply check the proper int bounds.
'''
'''
def reverse(x: int) -> int:
    if x == 0:
        return 0
    numStr = str(abs(x))
    revStr = numStr[::-1]
    answer = int(revStr)
    if x < 0:
        answer = -answer
    if answer > (2**31 - 1) or answer < -(2**31):
        return 0
    return answer
'''
'''I double ckecked the problem and it specifically does not allow 64-bit numbers
at any point, so I combined my earlier check with the simplified reversal for a
complete solution'''
def reverse(x: int) -> int: 
    if x == 0:
        return 0
    numStr = str(abs(x))
    revStr = numStr[::-1]
    if len(revStr) == 10:
        if int(revStr[0]) > 2:
            return 0
        elif int(revStr[0]) == 2:
            numCheck = int(revStr[1:])
            if x > 0:
                numCheck += 1
            if numCheck > 147483648:
                return 0
    answer = int(revStr)
    if x > 0:
        return answer
    else:
        return -answer

    
example1 = 8463847412
example2 = -8463847412
example3 = 9463847412
example4 = 7463847412
print(reverse(example1))
print(reverse(example2))
print(reverse(example3))
print(reverse(example4))
