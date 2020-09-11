#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 旋转数组中的最小数字.py
@time: 2020/02/18

"""

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

class Solution:
    def minNumberInRotateArray(self, rotate_array):
        if rotate_array == None or len(rotate_array) == 0:
            return  None

        index1 = 0
        index2 = len(rotate_array)-1
        mid_index = 0
        while rotate_array[index1] >= rotate_array[index2]:
            ## 当两个指针的距离是1时，表明两个指针分别指向两个递增数列的末尾和开头
            if index2 - index1 == 1:
                mid_index = index2
                break
            mid_index = (index2 + index1) // 2
            ## 如果下标为index1、index2和mid_index指向的三个数字相等
            ## 则只能顺序查找
            if rotate_array[index1] == rotate_array[index2] and \
                rotate_array[index2] == rotate_array[mid_index]:
                return  self.minInOrder(rotate_array, index1, index2)
            if rotate_array[index1] <= rotate_array[mid_index]:
                index1 = mid_index
            elif rotate_array[index2] >= rotate_array[mid_index]:
                index2 = mid_index
        return  rotate_array[mid_index]

    def minInOrder(self, array, front, rear):
        """顺序查找"""
        result = array[0]
        for i in range(front, rear):
            if array[i] < result:
                result = array[i]
        return  result



if __name__ == "__main__":
    Test = Solution()
    print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
    print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
    print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
    print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
    print(Test.minNumberInRotateArray([]))
    print(Test.minNumberInRotateArray([1]))