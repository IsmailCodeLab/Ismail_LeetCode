# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        stack.append(root)
        out=[]
        if root is None:
            return out
        while len(stack)>0:
            item=stack.pop()
            out.append(item.val)
            if item.right is not None:
                stack.append(item.right) 
            if item.left is not None:
                stack.append(item.left) 
        return out
            