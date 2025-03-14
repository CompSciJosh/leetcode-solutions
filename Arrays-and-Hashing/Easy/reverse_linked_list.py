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
#######################################
######### Option 1: Recursion #########
#######################################
# from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
#
#         return newHead

# Helper function to convert a list into a linked list
# def create_linked_list(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     current = head
#     for val in arr[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head
#
# # Helper function to print a linked list
# def print_linked_list(head):
#     current = head
#     result = []
#     while current:
#         result.append(str(current.val))
#         current = current.next
#     print(" -> ".join(result))
#
# # Test the function
# values = [1, 2, 3, 4, 5]  # Example linked list: 1 -> 2 -> 3 -> 4 -> 5
# head = create_linked_list(values)
#
# print("Original Linked List:")
# print_linked_list(head)
#
# # Reverse the linked list
# solution = Solution()
# reversed_head = solution.reverseList(head)
#
# print("Reversed Linked List:")
# print_linked_list(reversed_head)

###############################
##### Option 2: Iteration #####
###############################
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val # Stores the integer value of the node (default 0)
        self.next = next # A reference (pointer) to the next node (default None)
        # Example:
        # node1 = ListNode(5)
        # node2 = ListNode(7)
        # node1.next = node2  ...Links node1 (5) to node2 (7)

class Solution:
    # Means that a function parameter or return type can be either ListNode or None
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]: # function take head which is the first node of the linked list
        prev, curr = None, head # prev is initialized to None/Null (it will be the new last node) ... curr is set to head

        while curr: # Loop continues until we reach the end (curr = None)
            temp = curr.next # Stores next node (to avoid losing reference)
            curr.next = prev # Reverses the pointer of the current node
            prev = curr # Moves prev pointer forward
            curr = temp # Moves curr pointer to the next node
        return prev # prev will be the first node of the reversed list

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr: # Checks if the list is empty, if empty return None (i.e. no linked list is created)
        return None

    head = ListNode(arr[0]) # Create the first node using the first value of arr
    current = head # current points to head, which helps in adding new nodes later
    for val in arr[1:]: # Loops through all elements after the first one
        current.next = ListNode(val) # ListNode(val) creates a new node ... current.next links the new node to 'current.next'
        current = current.next # Moves current to this new node (to continue adding nodes)
    return head # After the loop, head still points to the first node of the linked list
    # Returns head so that the linked list can be used elsewhere

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

# Test the function
values = [5, 7, 9, 10, 11]  # Example linked list: 5 -> 7 -> 9 -> 10 -> 11
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
solution = Solution()
reversed_head = solution.reverse_list(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)