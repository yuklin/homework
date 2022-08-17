"""
    https://leetcode.cn/problems/deepest-leaves-sum/

    1302. 层数最深叶子节点的和
    给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
    
    
    
    示例 1：
    
    
    
    输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    输出：15
    示例 2：
    
    输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    输出：19
    
    
    提示：
    
    树中节点数目在范围 [1, 104] 之间。
    1 <= Node.val <= 100
    
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def travel(node, height):
    yield node.val, height
    if node.left:
        for i in travel(node.left, height + 1):
            yield i

    if node.right:
        for i in travel(node.right, height + 1):
            yield i



class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        tmp = []
        _max = 0

        for v, height in travel(root, 0):
            if height > _max:
                _max = height
                tmp = [v, ]
            elif height == _max:
                tmp.append(v)

        return sum(tmp)
