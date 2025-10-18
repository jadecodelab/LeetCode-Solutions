#Given a string sentence containing only lowercase English letters
#return true if sentence is a pangram, or false otherwise

def checkIfPangram(sentence:str)->bool:
    # add every letter of 'sentence' to hash set 'seen'
    seen = set(sentence)
    # if 'seen' has 26 letters, then 'sentence' is a pangram
    return len(seen)==26

# Time complexity: O(n)
# Space complexity: O(1)


s1 = "thequickbrownfoxjumpsoverthelazydog"
s2 = "thisisapangram"
print(s1)
print(checkIfPangram(s1))
print(s2)
print(checkIfPangram(s2))

    
    
