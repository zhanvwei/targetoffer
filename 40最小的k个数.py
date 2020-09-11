 #!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 40最小的k个数.py
@time: 2020/03/28

"""


'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
# 简单的思路： 先排序，快排(nlogn)
'''


class Solution:
    # 利用partition函数

    def getLeastNumbers(self, arra, k):
        # write code here
        if arra is None or len(arra) == 0 or\
            k > len(arra) or k <= 0:
            return []
        start = 0
        end = len(arra) - 1
        index = self.partition(arra, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition(arra, start, end)
            else:
                start = index + 1
                index = self.partition(arra, start, end)

        result = arra[:k]
        result.sort()
        return  result


    def partition(self, arra, start, end):
        # write code here
        if end == start:
            return  end
        # 选择分界点元素
        pivot = arra[start]
        left = start + 1
        right = end
        done = False
        # 从分界点元素的下一个元素开始遍历，将小于分界点值的元素放在其左边，
        # 将大于分界点值的元素放在其右边
        while not  done:
            while left <= right and arra[left] <= pivot:
                left += 1
            while left <= right and arra[right] >= pivot:
                right -= 1
            if left > right:
                done = True
            else: # 当左下标所指值大于分界值且右下标所指值小于分界值时，交换两下标元素值
                arra[left], arra[right] = arra[right], arra[left]
        arra[start], arra[right] = arra[right], arra[start]
        return  right


    ## 算法时间复杂度O(nlogk), 适合海量数据
    ## 利用一个k容量的容器存放数组, 构造最大堆,
    ## 当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数
    def getLeastNumbers2(self, arra, k):
        # write code here
        import heapq
        if arra is None or len(arra) == 0 or\
            k > len(arra) or k <= 0:
            return []
        result = []
        for i in arra:
            if len(result) < k:
                result.append(i)
            else:
                # 不推荐构造最小堆
                # 推荐构造最大堆
                result = heapq.nlargest(k, result)
                if i >= result[0]:
                    continue
                else:
                    result[0] = i
        return result[::-1]






if __name__ == "__main__":
    s = Solution()
    arra = [4,5,1,6,2,7,3,8]
    print(s.getLeastNumbers(arra, 2))
    print(s.getLeastNumbers2(arra, 2))
