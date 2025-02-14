# Joshua Jackson
# Problem: 1929. Concatenation of Array
# url: https://leetcode.com/problems/concatenation-of-array/description/
# Language: Python
# Difficulty: Easy

""" 
Description:

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000

"""

""" 
Beginning of Solution
"""
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
	# Option 1:
        # result = []
        # for num in nums:
        #     result.append(num)
        # for num in nums:
        #     result.append(num)
        # return result

	# Option 2:
        return nums * 2  # Repeat the list twice
"""
End of Solution
"""
numbers = [2, 4, 6, 8]

dbl_length = 2 * len(numbers)

solution = Solution()

combined_arr = solution.getConcatenation(numbers)

txt = f"The ans of length {dbl_length} is: {combined_arr}"

print(txt)
