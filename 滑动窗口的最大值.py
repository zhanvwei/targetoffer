#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 滑动窗口的最大值.py
@time: 2020/04/15

"""

'''
给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，它们的最大值分别为{4,4,6,6,6,5}。
'''

class Solution:
    def maxInWindows(self, arra, size):
        # write code here
        if arra is None or len(arra) <= 0 or\
            size < 0 or len(arra) < size:
            return []
        # 保存结果
        result = []
        # 模拟双向队列用于保存滑动窗口的最大值的下标
        # 当遍历的数小于队尾的数时，则添加到队尾，
        # 否则删除队尾元素，并将其添加到队尾
        deques = []
        # 第一个滑动窗口
        for i in range(size):
            while deques and arra[i] > arra[deques[-1]]:
                deques.pop()
            deques.append(i)

        for i in range(size, len(arra)):
            result.append(arra[deques[0]])
            while deques and arra[i] > arra[deques[-1]]:
                deques.pop()
            # 当队列的最大值的下标不在滑窗的范围内时，删除队列中的对头元素
            while deques and deques[0] <= i - size:
                deques.pop(0)
            deques.append(i)
        result.append(arra[deques[0]])
        return  result



if __name__ == "__main__":
    arra = [2, 3, 4, 2, 6, 2, 5, 1]
    s = Solution()
    print(s.maxInWindows(arra, 3))
