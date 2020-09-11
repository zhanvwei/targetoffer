#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 序列化二叉树.py
@time: 2020/03/22

"""
"""
实现两个函数，分别用来序列化和反序列化二叉树
"""

'''
思路： 通过前序遍历和中序遍历可以构造二叉树，但是该方法要求
      二叉树中不能有重复的节点；且只有当两个序列中的所有数
      读出来后才能开始反序列化。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root, strs):
        # write code here
        if root is None:
            return '$'
        strs = str(root.val) + ','
        strs += self.serialize(root.left, strs)
        strs += ','
        strs += self.serialize(root.right, strs)
        return  strs

    def deserialize(self, strs):
        # write code here
        serialize = strs.split(',')
        root, index = self._deserialize(serialize, 0)
        return  root

    def _deserialize(self, serialize, index):
        if index >= len(serialize) or serialize[index] == '$':
            return None, index + 1
        val = int(serialize[index])
        node = TreeNode(val)
        index += 1
        node.left, index = self._deserialize(serialize, index)
        node.right, index = self._deserialize(serialize, index)
        return  node, index




if __name__ == "__main__":
    pNode1 = TreeNode(1)
    pNode2 = TreeNode(2)
    pNode3 = TreeNode(3)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(5)
    pNode6 = TreeNode(6)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode3.left = pNode5
    pNode3.right = pNode6

    serializes = '1,2,4,$,$,$,3,5,$,$,6,$,$'

    ss = Solution()
    #result = ss.serialize(pNode1, '')
    root = ss.deserialize(serializes)
    #print(result)

    print(root.right.val)
