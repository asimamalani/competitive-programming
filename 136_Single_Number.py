"""
136. Single Number
Easy
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

class Solution:
    # brute force two loops time: O(n2) space: O(1)
    def singleNumberV1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if sum([1 for x in nums if x == num]) == 1:
                return num
        return -1
    
    # optimized Counter time: O(n) space: O(n)
    def singleNumberV2(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for key in counter:
            if counter[key] == 1:
                return key
        return -1
    
    # optimized Set time: O(n) space: O(n)
    def singleNumberV3(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num in unique:
                unique.remove(num)
            else:
                unique.add(num)
        return unique.pop()
    
    # optimized Math time and space: O(1) space: O(1)
    def singleNumberV4(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
    
    # optimized Bit time and space: O(1) space: O(1)
    def singleNumberV5(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a
