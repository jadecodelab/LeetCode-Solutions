# Given a string s, find the length of the longest substring without duplicate characters.

def lengthOfLongestSubstring(s:str) -> int:
    last = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1

        last[ch] = right
        best = max(best, right-left+1)

    return best


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
