#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数据流中的中位数.py
@time: 2020/03/29

"""

'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''


class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def insert(self, num):
        # write code here
        if self.count & 1 == 0:
            self.right.append(num)
        else:
            self.left.append(num)

    def getMedian(self, arra):
        # write code here
        if self.count == 1:
            return self.left[0]
        self.maxHeap(self.left)
        self.minHeap(self.right)
        # 如果最小堆的最小元素小于最大堆的最大元素，则交换值
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.maxHeap(self.left)
        self.minHeap(self.right)
        if self.count & 1 == 0:
            # arra的个数为偶数
            return (self.left[0] + self.right[0]) / 2.0
        else:
            return self.left[0]



    def maxHeap(self, right):
        # write code here
        # 实现二叉堆的上浮功能
        length = len(right)
        if right is None or len(right) <= 0:
            return
        if length == 1:
            return right
        for i in range(length//2 - 1, -1, -1):
            k = i
            temp = right[k]
            heap = False
            while not heap and 2*k < length - 1:
                index = 2*k + 1 # 左节点索引
                # 如果左孩子的值小于右孩子的值，则定位到右孩子
                if right[index] < right[index + 1] and index < length - 1:
                    index += 1
                if temp >= right[index]:
                    heap = True
                else:
                    # 否则将子节点的最大值复制给父节点，并定位到子节点
                    right[k] = right[index]
                    k = index
            right[k] = temp







    def minHeap(self, left):
        #write code here
        length = len(left)
        if left is None or len(left) <= 0:
            return
        if length == 1:
            return  left
        for i in (length//2 - 1, -1, -1):
            k = i
            temp = left[k]
            heap = False
            while not heap and 2*k < length - 1:
                index = 2*k + 1
                if left[index] > left[index + 1] and index < length -1:
                    index += 1
                if temp < left[index]:
                    heap = True
                else:
                    left[k] = left[index]
                    k = index
            left[k] = temp



if __name__ == "__main__":
    arra = [6, 8, 7, 6]
    s = Solution()

