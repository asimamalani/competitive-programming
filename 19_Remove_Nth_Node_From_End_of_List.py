"""
19. Remove Nth Node From End of List
Medium
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # brute force two pass time O(n), space O(1)
    def removeNthFromEndV1(self, head: ListNode, n: int) -> ListNode:
        sz, curr = 0, head
        while curr:
            sz += 1
            curr = curr.next
        del_idx = sz - n
        if del_idx == 0:
            head = head.next
            return head
        curr = head
        while del_idx-1 > 0:
            curr = curr.next
            del_idx -= 1
        curr.next = curr.next.next
        return head
    
    # optimized one pass time O(n), space O(1)
    def removeNthFromEndV2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        first = second = dummy
        for i in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
