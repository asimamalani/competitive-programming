"""
98. Validate Binary Search Tree
Medium
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive traversal with valid range time O(n), space O(n)
    def isValidBSTV1(self, root: TreeNode) -> bool:
        def isValidBSTHelper(node, low, high):
            if not node:
                return True
            if not (low <= node.val <= high):
                return False
            return isValidBSTHelper(node.left, low, node.val-1) and isValidBSTHelper(node.right, node.val+1, high)
        
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        return isValidBSTHelper(root, INT_MIN, INT_MAX)
    
    # iterative traversal with valid range time O(n), space O(n)
    def isValidBSTV2(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, low, high = stack.pop()
            if not root:
                continue
            if not (low <= root.val <= high):
                return False
            stack.append((root.left, low, root.val-1))
            stack.append((root.right, root.val+1, high))
        return True
    
    # inorder recursive
    def isValidBSTV3(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)
    
    # inorder iterative
    def isValidBSTV4(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
