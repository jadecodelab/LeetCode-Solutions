#Given an array of integers nums, find the maximum value of
#nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum
#Return -1 if there is no pair of numbers with the same digit sum.

from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        #helper function to get sum of the digits of a number
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            
            return digit_sum
        
        dic = defaultdict(int) #store numbers grouped by digit sum
        ans = -1  
        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in dic:
                ans = max(ans, num + dic[digit_sum])
            dic[digit_sum] = max(dic[digit_sum], num)

        return ans


nums = [12,10,53,21,35]
ans = Solution()
print(ans.maximumSum(nums))

