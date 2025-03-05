# Joshua Jackson
# Problem: 20. Valid Parentheses
# url: https://leetcode.com/problems/valid-parentheses/description/
# Language: Python
# Difficulty: Easy
"""
Description: Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true
Example 2:
    Input: s = "()[]{}"
    Output: true
Example 3:
    Input: s = "(]"
    Output: false
Example 4:
    Input: s = "([])"
    Output: true

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

"""*************** Code Below ***************"""
""" 
Beginning of Solution
"""
class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]" : "[", "}" : "{"} # key:value pairs

        for c in s: # for every char in the string
            if c in close_to_open: # if the char, which is a key, is in the dictionary close_to_open
                """ if the stack is not empty and the value at the top of the stack 
                    is equivalent to the value of the key:value pair"""
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop() # pop the value at the top of the stack
                else: # else the stack is empty, we can not add a closing symbol to the stack, return False
                    return False
            else: # if the symbol read is not in a key in close_to_open then add it to the top of the stack
                stack.append(c)

        return True if not stack else False # return True if the stack is empty but if it is not empty return False
"""
End of Solution
"""
symbols_1 = "[]{}(){}"
symbols_2 = "({[{}]})}"
solution = Solution()
result = solution.is_valid(symbols_2)
print(result)


