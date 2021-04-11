"""
1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution:
    # brute force two loops time O(n2), space O(1)
    def twoSumV1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
    
    # optimize time O(n), space O(n)
    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, elem in enumerate(nums):
            comp = target-elem
            if comp in lookup:
                return [lookup[comp], i]
            lookup[elem] = i
        return None
