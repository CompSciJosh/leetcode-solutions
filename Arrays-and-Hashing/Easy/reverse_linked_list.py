# Joshua Jackson
# Problem: 206. Reverse Linked List
# url: https://leetcode.com/problems/reverse-linked-list/description/
# Language: Python
# Difficulty: Easy

"""
Description:

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Initially:  1 -> 2 -> 3 -> 4 -> 5
    Final: 5 -> 4 -> 3 -> 2 -> 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
    Initially:  1 -> 2
    Final: 2 -> 1

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

"""*************** Code Below ***************"""
""" 
Beginning of Solution
"""
#############################
######### Recursion #########
#############################
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

# Helper function to convert a list into a linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

# Test the function
values = [1, 2, 3, 4, 5]  # Example linked list: 1 -> 2 -> 3 -> 4 -> 5
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)