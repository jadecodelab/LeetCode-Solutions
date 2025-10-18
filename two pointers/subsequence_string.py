def is_subsequence(s,t):
    i=j=0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    return i==len(s)


s="abc"
t="arbdvcg"
l="gmsi"

if is_subsequence(s,t):
    print("s is subsequence of t")
else:
    print("s is NOT subsequence of t")

if is_subsequence(s,l):
    print("s is subsequence of l")
else:
    print("s is NOT subsequence of l")
