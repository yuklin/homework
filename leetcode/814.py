'''
    https://leetcode.cn/problems/binary-tree-pruning/

    给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。

    返回移除了所有不包含 1 的子树的原二叉树。

节点 node 的子树为 node 本身加上所有 node 的后代。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-pruning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#def travel(node):
#    if not node:
#        return 0
#
#    s_L = travel(node.left)
#
#    if not s_L:
#        node.left = None
#   
#    s_R = travel(node.right)
#    
#    if not s_R:
#        node.right = None
#
#    return node.val + s_L + s_R
#
#class Solution:
#    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#        travel(root)
#        if root.val == 0 and not root.left and not root.right:
#            return None
#        return root
#

# 可以直接剪的
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        
        if root.val == 0 and not root.left and not root.right:
            return None
        return root
