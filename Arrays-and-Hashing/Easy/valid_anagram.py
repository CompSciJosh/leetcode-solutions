# Joshua Jackson
# Problem: 242. Valid Anagram
# url: https://leetcode.com/problems/valid-anagram/description/
# Language: Python
# Difficulty: Easy

"""
Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

""" 
Beginning of Solution
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for num in count:
            if num != 0:
                return False
        return True

"""
End of Solution
"""

word_1, word_2 = "batman", "manbat"

solution = Solution()

same_letters = solution.isAnagram(word_1, word_2)

lowercase_bool = str(same_letters).lower()

txt = f"It is {lowercase_bool} that {word_1} and {word_2} have the same letters and are anagrams."

print(txt)

