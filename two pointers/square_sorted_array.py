from typing import List

def sortSquares(nums:List[int])->List[int]:
    n = len(nums)
    result = [0]*n
    left = 0
    right = n-1
    for i in range(n-1, -1, -1):
        if abs(nums[left])<abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square*square
    return result

a=[-4,-2,0,3,10]
print(sortSquares(a))
                
