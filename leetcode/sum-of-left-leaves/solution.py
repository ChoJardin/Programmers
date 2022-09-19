// [문제 링크]: https://leetcode.com/problems/sum-of-left-leaves/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right: 
            return 0
        
        ans = 0
        
        def get_sum(tree, is_left):
            nonlocal ans
            
            # 왼쪽 자식이 있음
            if tree.left:
                get_sum(tree.left, True)
                
            # 오른쪽 자식이 있음 
            if tree.right: 
                get_sum(tree.right, False)
            
            # 리프노드 
            if not tree.left and not tree.right: 
                if is_left: 
                    ans += tree.val
        
        get_sum(root, False)
            
        return ans