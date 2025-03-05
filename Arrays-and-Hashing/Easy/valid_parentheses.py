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
        stack = [] # dynamic list; Python list
        close_to_open = {")": "(", "]" : "[", "}" : "{"} # dictionary - key:value pairs

        for c in s: # for every char in the string
            if c in close_to_open: # if the char, which is a key, is in the dictionary close_to_open
                """ if the stack is not empty and the value at the top of the stack 
                    is equivalent to the value of the key:value pair"""
                if stack and stack[-1] == close_to_open[c]: # passing in the closing symbol and getting the open symbol
                    stack.pop() # pop the value at the top of the stack
                else: # if they don't match or the stack is empty, return False b/c it means the symbols do not match
                    return False
            else: # this means it must be an open symbol so the symbol read is not a key in close_to_open then add it to the top of the stack.
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

"""
Time Complexity: O(n) <- b/c we have to go through each input character, n, once.
Space Complexity: O(n) <- b/c the stack could be up to the size of the input, n.
"""

