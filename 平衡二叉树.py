#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 平衡二叉树.py
@time: 2020/04/13

"""

"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，则为一棵二叉树。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.is_balance = True

    def getDepth(self, root):
        # write code here
        if root is None:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def isBalanced1(self, root):
        # write code here
        if root is None:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False
        return self.isBalanced1(root.left) and self.isBalanced1(root.right)


    # 采用后序遍历，则只需遍历一次
    def isBalanced2(self, root):
        # write code here
        if root is None:
            return True

        def postOrder(root, ):
            if self.is_balance is False:
                return -1
            if root is None:
                return 0
            left = postOrder(root.left)
            right = postOrder(root.right)
            if abs(left - right) > 1:
                self.is_balance = False
            return max(left, right) + 1

        postOrder(root)
        return self.is_balance







if __name__ == "__main__":
    pNode1 = TreeNode(1)
    pNode2 = TreeNode(2)
    pNode3 = TreeNode(3)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(5)
    pNode6 = TreeNode(6)
    pNode7 = TreeNode(7)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.right = pNode6
    pNode5.left = pNode7

    s = Solution()
    print(s.isBalanced1(pNode1))