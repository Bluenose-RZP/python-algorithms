'''Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
'''
'''This was my first attempt. It took me a while. The only major bug while coding
was in the for loop, I wrote as 'for i, word in strs' took me a bit to switch
to enumerate.  It wasn't very efficient. It took more than O(n^2) time, but it
at least worked.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [] #the list of anagrams grouped to be returned
        dicts = [] #the list of anagram dictionaries
        for i, word in enumerate(strs):
            wasPresent = False
            thisWord = {}
            for char in word: # after this, thisWord contains a count of each char
                thisWord[char] = thisWord.get(char, 0) + 1
            for i, checkWord in enumerate(dicts):
                if checkWord == thisWord:
                    anagrams[i].append(word) # if the current word anagram exists, add to anagrams and stop check, then skip to next word
                    wasPresent = True
                    break
            if wasPresent:
                continue
            dicts.append(thisWord)
            anagrams.append([word])
        return anagrams
        '''
'''This version has many improvements. Instead of checking through a dictionary,
it uses  character count tuple instead of a character dictionary to sort.
It uses the tuple as the key in anagrams and the individual strings as lists under
that key instead of storing the lists separate from the list of dictionary values.
the runtime has gone to O(n), much better.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())
