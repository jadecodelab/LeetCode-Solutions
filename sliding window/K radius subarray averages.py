#The k-radius average for a subarray of nums centered at
#some index i with the radius k is the average of all
#elements in nums between the indices i - k and i + k (inclusive)
#If there are less than k elements before or after the index i
#then the k-radius average is -1

from typing import List

def getAverage(nums:List[int],k:int)->List[int]:   
    averages = [-1]*len(nums) 
    if k == 0:      #if radius=0, there is only one element in the subarray, 
        return nums #so the average of one element is just itself

    sub_size = 2*k+1 #subarray size
    if sub_size > len(nums):   #if subarray size is greater than the array size
        return averages #the averages will be -1 as what was initiated

    sub_sum = sum(nums[:sub_size]) #sum of the first subarray
    averages[k] = sub_sum//sub_size

    for i in range(sub_size,len(nums)):
        sub_sum += nums[i] - nums[i-sub_size]
        averages[i-k] = sub_sum//sub_size

    return averages

# time complexity: O(n)
# space complexity: O(1)

nums = [7,4,3,9,1,8,5,2,6]
k = 2
print(getAverage(nums,k))
