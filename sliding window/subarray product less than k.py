# given an array of positive integers nums and an integer k
# find the number of subarrays where product of all elements is less than k

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self,nums:List[int],k:int)->int:
        if k <= 1:
            return 0 # because all elements are positive integers >=1,
                     # no subarray can have a product less than 1
        ans = left = 0
        curr = 1 # initiallize the product of a elements of current window

        for right in range(len(nums)):
            curr *= nums[right]
            if curr >= k:
                curr /= nums[left]
                left += 1
            ans += right-left+1 # numbers of subarrays
        return ans

# this algorithm has a runtime of O(n) and O(1) space

# test the function

nums = [10, 5, 2, 6]
k = 100

sol = Solution()
ans = sol.numSubarrayProductLessThanK(nums,k)
print(ans)
