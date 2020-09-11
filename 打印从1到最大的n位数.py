#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 打印从1到最大的n位数.py
@time: 2020/02/24

"""

'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''

class Solution:
    def printToMaxOfDigits(self, n):
        """依次打印从1到最大的n位十进制数"""
        if n <= 0:
            return
        number = ['0']*n
        while not self.increment(number):
            self.printNumber(number)


    def increment(self, number):
        """
        模拟数字加法
        当加1时第一个字符产生进位，则表示已经是最大的n位数，此时返回True
        """
        is_over_flow = False
        n_take_over = 0
        length = len(number)
        for i in range(length - 1, -1, -1):
            ## 将各数位上的字符转换成数字，若有进位则加1
            sums = int(number[i]) + n_take_over
            ## 个位加1
            if i == length - 1:
                sums += 1
            if sums >= 10:
                if i == 0:
                    is_over_flow = True
                else:
                    sums -= 10
                    n_take_over = 1
                    number[i] = str(sums)
            else:
                number[i] = str(sums)
                #print(number[i])
                break
        return  is_over_flow



    def printNumber(self, number):
        """从数位第一个不为0的数字开始打印数字"""
        is_beginning0 = True
        length = len(number)
        for i in range(length):
            if is_beginning0 and number[i] != '0':
                is_beginning0 = False
            if not is_beginning0:
                print('%c' % number[i], end= '')
        print('')


if __name__ == "__main__":
    ss = Solution()
    ss.printToMaxOfDigits(3)