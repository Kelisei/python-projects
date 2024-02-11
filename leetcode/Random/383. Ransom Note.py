# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

 

# Constraints:

#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.

#!FOR THIS WE MUST USE HASHTABLES, USING THE COUNTER OBJECT 
#!Counter is useful when determining the frequency of stuff, in this case Counter creates a hashtable with the keys being the char and a counter which is the number of apparitions.
#!When we find a element that is in the table we decrement the frecuency, if it's negative you return false. Else is true.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = Counter(magazine)
        for char in ransomNote:
            if char in chars:
                chars[char] -= 1
                if chars[char] < 0:
                    return False
            else:
                return False
        return True
