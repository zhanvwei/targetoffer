#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二叉树中和为某一值的所有路径.py
@time: 2020/03/18

"""
'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 分析思路：当访问某一节点时，将该节点添加到当前路径，并累加该节点的值，
    #         分情况：a. 该节点为叶节点时，若路径符合要求，则添加到result，并返回其父节点，并删除其值；
    #                b. 该节点不是叶节点，则继续访问其子节点；
    def findSumPath(self, root, target):
        # write code here
        if root is None:
            return  []
        result = []
        def findSumPathMain(root, path, current_sum):
            current_sum += root.val
            path.append(root.val)

            # 是否是叶节点
            is_leaf = root.left is None and root.right is None
            # 如果当前值等于目标值，且当前节点为叶节点则将当前路径添加到result
            if is_leaf and current_sum == target:
                result.append(path[:])
            else:
                # 如果当前节点不为叶节点，则遍历其子节点
                if root.left is not  None:
                    print(root.left.val)
                    findSumPathMain(root.left, path, current_sum)
                if root.right is not None:
                    findSumPathMain(root.right, path, current_sum)

            # 返回父节点前，删除当前路径的当前节点
            print(path, current_sum)
            path.pop()
        findSumPathMain(root, [], 0)

        return  result


if __name__ == "__main__":
    pNode1 = TreeNode(10)
    pNode2 = TreeNode(5)
    pNode3 = TreeNode(12)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(7)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5

    S = Solution()
    print(S.findSumPath(pNode1, 22))