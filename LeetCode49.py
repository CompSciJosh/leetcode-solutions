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