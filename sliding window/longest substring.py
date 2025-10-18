# given a binary string s (a string containing only "0" and "1").
# choose up to one "0" and flip it to a "1".
# return the length of the longest substring achievable that contains only "1"

def find_length(s):
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right]== "0":
            curr += 1 #number of "0" in the window
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans,right-left+1) #return max length of the window
    return ans

# test function
s = "1101100111"
print(find_length(s))
            
