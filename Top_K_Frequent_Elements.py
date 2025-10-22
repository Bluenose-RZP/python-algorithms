'''Given an integer array nums and an integer k, return the k most frequent elements.
you may return the answer in any order.
Follow up: ensure the algorithm's time complexity is better than 0(n log n) where
n is the array size.

I had some trouble finding out how to use the sorted function here. I'd not seen 
lambda anonymous functions before. I think I'll need to study that concept more
to get the most out of it. My solution worked well though, however it used 0(n log n)
efficiency so I still need to do the followup.
''' 

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        freqList = list(freqs.items())
        freqSorted = sorted(freqList, key=lambda x: x[1], reverse=True)
        answers = [item[0] for item in freqSorted]
        return answers[:k]
