# Joshua Jackson
# Problem: 155. Min Stack
# url: https://leetcode.com/problems/min-stack/description/
# Language: Python
# Difficulty: Medium
# Companies: Amazon

"""
Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

"""

"""*************** Code Below ***************"""
""" 
Beginning of Solution
"""

class MinStack:

    def __init__(self):
        # First initialize your data structures
        # We know we are going to have two stacks (i.e. Python lists)
        self.stack = []
        self.least_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        least_val = min(val, self.least_stack[-1] if self.least_stack else val)
        self.least_stack.append(least_val)

    def pop(self) -> None:
        self.stack.pop()
        self.least_stack.pop()

    def top(self) -> int:
        result = self.stack[-1]
        return result

    def get_min(self) -> int:
        minimum = self.least_stack[-1]
        return minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""
Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
"""
solution = MinStack()
solution.push(-2)
solution.push(0)
solution.push(-3)
min_val = solution.get_min()
print(min_val)
solution.pop()
solution.top()
min_val = solution.get_min()
print(min_val)