#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数组中的逆序对.py
@time: 2020/04/07

"""
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''

class Solution:
    def inversePairs1(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0]*length
        for i in range(length):
            copy[i] = data[i]

        count = self.inversePairsCore(data, copy, 0, length-1)
        return count
    def inversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start)//2
        left = self.inversePairsCore(copy, data, start, start+length)
        right = self.inversePairsCore(copy, data, start+length+1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count


    def inversePairs2(self, alist):
        # write code here
        if len(alist) <= 0:
            return 0
        counts = 0
        copy = [i for i in alist]
        copy.sort()
        print(copy)
        i = 0
        while i < len(copy):
            counts += alist.index(copy[i])
            alist.remove(copy[i])
            i += 1
        return counts



if __name__ == "__main__":
    s = Solution()
    res1 = s.inversePairs1([7,5, 6, 4])
    res2 = s.inversePairs2([7,5, 6, 4])
    print(res1)
    print(res2)