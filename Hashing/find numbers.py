def find_numbers(nums):
    ans =[]
    nums_set = set(nums)
    for n in nums_set:
        if (n+1 not in nums_set) and (n-1 not in nums_set):
            ans.append(n)
    return ans

nums = [1,2,3,34,5]
print(find_numbers(nums))
