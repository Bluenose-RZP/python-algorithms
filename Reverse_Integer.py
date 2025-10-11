def reverse(x: int) -> int: #Reverses an int x staying within 32-bit bounds
    if x == 0:
        return 0
    numStr = str(abs(x)) #Convert x to string
    revStr = numStr[::-1] #Reverse the string
    if len(revStr) == 10: #Check for overflow as a string
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
