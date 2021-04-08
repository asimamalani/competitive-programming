"""
189. Rotate Array
Medium

4368

918

Add to List

Share
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:
    # Brute force: Time Complexity O(n2), Space Complexity: O(1)
    def rotateV1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2 or (k % n) == 0:
            return
        k = k % n
        for _ in range(k):
            last = nums[-1]
            for i in range(n):
                nums[i], last = last, nums[i]
    
    # Optimized: Time Complexity O(n), Space Complexity: O(1)
    def rotateV2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2 or (k % n) == 0:
            return
        k = k % n
        
        def reverse_list(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
        
        reverse_list(nums, 0, n-1)
        reverse_list(nums, 0, k-1)
        reverse_list(nums, k, n-1)
