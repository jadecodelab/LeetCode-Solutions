#Given an array nums. We define a running sum of an array as
#runningSum[i] = sum(nums[0]…nums[i])
#Return the running sum of nums

from typing import List

class Solution:
    def runningSum(self,nums:List[int])->list[int]:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        return prefix
     


sol = Solution()
nums = [1,1,1,1,1]
print(sol.runningSum(nums))

#Time complexity: O(n)
#Space complexity: O(1)
