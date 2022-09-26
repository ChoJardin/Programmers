// [문제 링크]: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [] 
        
        def rearrange(level, sub_tree):
            nonlocal ans 
            
            if len(ans) < level + 1: 
                ans.append([sub_tree.val])

            else: 
                ans[level].append(sub_tree.val)
            
            if sub_tree.left: 
                rearrange(level+1, sub_tree.left)
            
            if sub_tree.right: 
                rearrange(level+1, sub_tree.right)
        
        if root: 
            rearrange(0, root)
            
        return ans