# Given an integer array cards, find the length of the shortest subarray that
# contains at least one duplicate. If the array has no duplicates, return -1.

from collections import defaultdict
from typing import List

def minumumCardPickup(cards:List[int])->int:
    dic = defaultdict(int)
    ans = float("inf")
    for i in range(len(cards)):
        if cards[i] in dic:
            ans = min(ans, i-dic[cards[i]]+1)
        else:
            dic[cards[i]] = i

    return ans if ans < float("inf") else -1

cards = [3,2,4,3,7,8,8]
print(minumumCardPickup(cards))
