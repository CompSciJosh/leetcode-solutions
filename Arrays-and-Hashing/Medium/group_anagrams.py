# Joshua Jackson
# Problem: 49. Group Anagrama
# url: https://leetcode.com/problems/group-anagrams/description/
# Language: Python
# Difficulty: Medium

"""
Description:
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

"""*************** Code Below ***************"""
from collections import defaultdict
from typing import List
""" 
Beginning of Solution
"""
class Solution: # could remove 'class Solution:' and 'self', unindent function, then uncomment 'def __init__(self): pass'
    def groupanagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            result[key].append(s)
        return list(result.values())
"""
End of Solution
"""

# class Solution:
#     def __init__(self):
#         pass


words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]

solution = Solution()

groups = solution.groupanagrams(words)

txt = f"The groups of anagrams are: {groups}"

print(txt)
