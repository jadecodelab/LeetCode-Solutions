#Given a binary array nums and an integer k,
#return the maximum number of consecutive 1's
#in the array if you can flip at most k 0's.

from typing import List

class Solution:
    def longestOnes(self,nums:List[int],k:int)->int:
        left = 0 #left pointer of the sliding window
        count = 0 #number of 0s in the window
        ans = 0 #the length of the window
        for right in range(len(nums)):
            if nums[right]==0:
                count += 1
            while count > k:
                if nums[left]==0:
                    count -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans


# Test solution
solution = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(solution.longestOnes(nums,k))

# Time complexity: O(N), where N is the the number of elements in the array
# Space complexity: O(1)
