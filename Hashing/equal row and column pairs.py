#Given an n x n matrix grid, return the number of pairs (R, C)
#where R is a row and C is a column, and R and C are equal
#if we consider them as 1D arrays.

from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid:List[List[int]]) -> int:
        def convert_to_key(arr):
            return tuple(arr)

        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1

        dic2 =defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])

            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr]*dic2[arr]

        return ans

# Test Case
answer = Solution()
grid = [
 [3, 1, 2, 2],
 [1, 4, 4, 5],
 [2, 4, 2, 2],
 [2, 4, 2, 2]
]
print(answer.equalPairs(grid))
