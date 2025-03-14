# Joshua Jackson
# Problem: 27. Remove Element
# url: https://leetcode.com/problems/remove-element/description/
# Language: Python
# Difficulty: Easy

"""
Description:

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

"""*************** Code Below ***************"""
"""
Beginning of Solution
"""

from typing import List

class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        for i in range (n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
"""
End of Solution
"""

arr = [2,4,3,0,4,4,5]
value = 4

solution = Solution()

print(f"The original integer array is {arr}.")

not_equal_to_val = solution.remove_element(arr, value)

print(f"k = {not_equal_to_val}")

txt = f"The value to be removed is {value}.\nThe first {not_equal_to_val} elements are not equal to {value} in the updated array.\nUpdated array: {arr}"

print(txt)

#########################

nums_array = [5, 3, 4, 1, 1, 6, 0, 1]
print(f"\nThe original integer array is {nums_array}.")

target_value = 1
print(f"The value to be removed is {target_value}.")

number_of_elements = solution.remove_element(nums_array, target_value)

# print("The number of unique values in the array are: ")
print (f"k = {number_of_elements}")
print(f"The first {number_of_elements} elements of nums contain the elements which are not equal to val.")
print(nums_array)
