#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二叉搜索树的后序遍历.py
@time: 2020/03/18

"""

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''



class Solution:
    def verifySequenceOfBST(self, sequence):
        if sequence is None or sequence == []:
            return  False
        length = len(sequence)
        root = sequence[-1]
        if min(sequence) > root or max(sequence) < root:
           return True

        # 记录左子树和右子树的分割点的坐标
        i_idx = 0
        for i in range(length - 1):
            if sequence[i] > root:
                break
            i_idx = i

        for j in range(i_idx+1, length - 1):
            if sequence[j] < root:
                return  False
        # 判断左子树是不是二叉树
        left = True
        if i_idx > 0:
            # 注意这里的是i_idx，否则在测试root结点前的所有元素小于root的情况时，
            # 本应返回True，但结果因为[]而返回False
            left = self.verifySequenceOfBST(sequence[:i_idx])
        # 判断右子树是不是二叉树
        right = True
        if i_idx < length - 1:
            right = self.verifySequenceOfBST(sequence[i_idx: length - 1])
        return  left and right


if __name__ == "__main__":
    array = [5, 7, 6, 9, 11, 10, 8]
    array2 = [7, 4, 6, 5]
    array3 = [1, 2, 3, 4, 5]
    S = Solution()
    print(S.verifySequenceOfBST(array))
    print(S.verifySequenceOfBST(array2))
    print(S.verifySequenceOfBST(array3))

