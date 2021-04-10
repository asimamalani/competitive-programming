"""
350. Intersection of Two Arrays II
Easy
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted. 

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
class Solution:
    # brute force two loops time O(n2), space O(1)
    def intersectV1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        while nums1:
            num = nums1.pop()
            for i in range(len(nums2)):
                if nums2[i] == num:
                    res.append(num)
                    del nums2[i]
                    break
        return res
    
    # optimized time sort and binary search on bigger array O(nLogn), space O(1)
    def intersectV2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(arr, item):
            lo, hi = 0, len(arr)-1
            while lo <= hi:
                mid = lo + (hi-lo) // 2
                if arr[mid] == item:
                    return mid
                elif arr[mid] < item:
                    lo = mid+1
                else:
                    hi = mid-1
            return -1 # item not found in a given array
        
        nums1.sort(), nums2.sort()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        while nums1:
            elem = nums1.pop()
            found_index = binary_search(nums2, elem)
            if found_index > -1:
                res.append(elem)
                del nums2[found_index]
        return res
    
    # optimized time Dict/Hashmap O(min(n, m)), space O(n+m)
    def intersectV3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        counter1, counter2 = collections.Counter(nums1), collections.Counter(nums2)
        for key in counter1:
            if key in counter2:
                res += [key] * min(counter1[key], counter2[key])
        return res
