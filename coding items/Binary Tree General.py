# 1. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Example 1:
# Input: root = [3,9,20,null,null,15,7].  Output: 3
# Example 2:
# Input: root = [1,null,2]. Output: 2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)



# 2. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Example 1: Input: p = [1,2,3], q = [1,2,3]. Output: true
# Example 2: Input: p = [1,2], q = [1,null,2]. Output: false
# Example 3: Input: p = [1,2,1], q = [1,1,2]. Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False



# 3. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.
# Example 1: Input: root = [4,2,7,1,3,6,9]. Output: [4,7,2,9,6,3,1]
# Example 2: Input: root = [2,1,3]. Output: [2,3,1]
# Example 3: Input: root = []. Output: []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root: # base case
            return root
        
        self.invertTree(root.left) # call the left substree
        self.invertTree(root.right) # call the right substree

        # swap the nodes
        root.left, root.right = root.right, root.left
        return root 



# 4. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Example 1: Input: root = [1,2,2,3,4,4,3]. Output: true
# Example 2: Input: root = [1,2,2,null,3,null,3]. Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root: # special case
            return True
        
        return self.isMirror(root.left, root.right) # return the function recursively
    
    def isMirror(self, leftroot, rightroot):
        if not leftroot and not rightroot:
            return True
        if not leftroot or not rightroot:
            return False
        
        if leftroot.val != rightroot.val:
            return False
        
        return self.isMirror(leftroot.left, rightroot.right) and self.isMirror(leftroot.right, rightroot.left)



# 5. Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]. Output: [3,9,20,null,null,15,7]
# Example 2:
# Input: preorder = [-1], inorder = [-1]. Output: [-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.index = 0

        def build(start, end):
            if start > end:
                return None
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)

            mid = idx_map[root_val]
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            return root

        return build(0, len(inorder) - 1)
        


# 6. Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
# Example 1: Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]. Output: [3,9,20,null,null,15,7]
# Example 2: Input: inorder = [-1], postorder = [-1]. Output: [-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index: -1])

        return root
        


# 7. Populating Next Right Pointers in Each Node II
# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Example 1: Input: root = [1,2,3,4,5,null,7]. Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2: Input: root = []. Output: []


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        from collections import deque
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                

        return root



# 8. Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
# Example 1: Input: root = [1,2,5,3,4,null,6]. Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2: Input: root = []. Output: []
# Example 3: Input: root = [0]. Output: [0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        self.flatten(root.right) # process right subtree first
        self.flatten(root.left)# process left
        root.right = self.prev
        root.left = None # set the current node's right to prev and left to null
        self.prev = root # update prev to current node

        

# 9. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
# Example 1: Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22. Output: true
# Example 2: Input: root = [1,2,3], targetSum = 5. Output: false
# Explanation: There are two root-to-leaf paths in the tree: (1 --> 2): The sum is 3. (1 --> 3): The sum is 4. There is no root-to-leaf path with sum = 5.
# Example 3: Input: root = [], targetSum = 0. Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum


# 10. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.
# Example 1: Input: root = [1,2,3]. Output: 25
# Explanation: The root-to-leaf path 1->2 represents the number 12. The root-to-leaf path 1->3 represents the number 13. Therefore, sum = 12 + 13 = 25.
# Example 2: Input: root = [4,9,0,5,1]. Output: 1026
# Explanation: The root-to-leaf path 4->9->5 represents the number 495. The root-to-leaf path 4->9->1 represents the number 491. The root-to-leaf path 4->0 represents the number 40. Therefore, sum = 495 + 491 + 40 = 1026.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node, p):
            if not node:
                return 0
        
            p = p * 10 + node.val
            if not node.left and not node.right:
                return p
            return dfs(node.left, p) + dfs(node.right, p)
        
        return dfs(root, 0)
        


# 11. Binary Tree Maximum Path Sum
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Example 1: Input: root = [1,2,3] Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2: Input: root = [-10,9,20,null,null,15,7]. Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return 0
            
            leftMaxPath = max(dfs(node.left), 0) # dont take LMP if it is negative

            rightMaxPath = max(dfs(node.right), 0) # dont take RMP if it is negative

            maxIfNodeIsRoot = node.val + leftMaxPath + rightMaxPath
            self.maxSum = max(self.maxSum, maxIfNodeIsRoot)
            return node.val + max(leftMaxPath, rightMaxPath)
        
        self.maxSum = float('-inf')
        dfs(root)
        return self.maxSum



