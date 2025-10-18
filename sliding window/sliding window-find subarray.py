
#Given an integer array nums and an integer k,
#find the sum of the subarray with the largest sum whose length is k

def find_best_subarray(nums,k):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k,len(nums)):
        curr += nums[i]-nums[i-k]
        ans = max(ans,curr)

    return ans

nums = [3,1,6,4,9,5]
k = 3
print(find_best_subarray(nums,k))

#Time complexity of O(n), using O(1) space
