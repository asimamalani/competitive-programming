"""
217. Contains Duplicate
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    # brute force Two loops. time: O(n2), space: O(1)
    def containsDuplicateV1(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # time optimized, Sorting. O(nlogn), space O(1)
    def containsDuplicateV2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        nums.sort()
        for i in range(n):
            if nums[i] == nums[i+1]:
                return True
        return True
    
    # time optimized, Counter Dict. O(n), space O(n)
    def containsDuplicateV3(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        counter = collections.Counter(nums)
        for key in counter:
            if counter[key] > 1:
                return True
        return False
    
    # time optimized, Set O(n), space O(n)
    def containsDuplicateV4(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        return n != len(set(nums))
    
    # time optimized, Set optimized O(n), space O(n)
    def containsDuplicateV5(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        lookup = set()
        for num in nums:
            if num in lookup:
                return True
            lookup.add(num)
        return False
