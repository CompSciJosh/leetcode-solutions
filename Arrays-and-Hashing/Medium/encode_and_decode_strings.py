# Joshua Jackson
# Problem *Premium Problem* ->: 271. Encode and Decode Strings
# url: *Free* -> https://www.lintcode[.]com/problem/659/
# Language: Python
# Difficulty: Medium

"""
Description:

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["my", "lovely", "wife"]
Output: ["my", "lovely", "wife"]

Example 2:
Input: [":"]
Output: [":"]

Example 3:
Input: []
Output:[]

"""

"""*************** SOLUTION ***************"""


class Solution:
# Example Input: ["my", "queen", "i", "love", "you"]
# Example Output: ["my", "queen", "i", "love", "you"]
    def encode(self, strs: List[str]) -> str:
        res = " "

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':  # Ensure we don't go out of bounds
                j += 1

            if j == len(s):  # Check if '#' was not found
                return res

            length = int(s[i:j])  # Extract the length
            res.append(s[j+1:j+1+length])  # Extract the substring
            i = j + 1 + length  # Move to the next segment
            
        return res