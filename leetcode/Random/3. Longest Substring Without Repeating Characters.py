# Given a string s, find the length of the longest
# substring
# without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        chars = set()
        for i, char in enumerate(s):
            while char in chars:
                chars.remove(s[start])
                start += 1
            chars.add(char)
            max_len = max(max_len, i - start + 1)
        return max_len

''' 
    Algorithm:
    We use the sliding window technique.
    -We use max_len and start as pointers to keep track of the substring.
    -We create a set to add all the unique characters.
    -We iterate over the string, for each character we:
        -While the char is in the substring we remove the character at start, and increment it to shrink the substring.
        This way it only contains unique characters.
        -We add the char to the substring.
        -We update max_len, if the current substring is larger (i - start +1) we update it.

'''