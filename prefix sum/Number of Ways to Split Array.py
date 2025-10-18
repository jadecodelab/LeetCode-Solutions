
#2270. Number of Ways to Split Array
#Given an integer array nums, find the number of ways
#to split the array  into two parts so that the first
#section has a sum greater than or equal to the sum of the second section.
#The second section should have at least one number.

from typing import List

class Solution:
    def waysToSplitArray(self,nums:List[int])->int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans

     

#Test solution
sol = Solution()
nums = [10,4,-8,7]
print(sol.waysToSplitArray(nums))

#Time complexity O(n)
#Space O(1)
