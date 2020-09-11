#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 扑克牌中的顺序.py
@time: 2020/04/23

"""
'''
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
'''

class Solution:
    def isContinuous(self, arra):
        """
        :type arra: list
        :rtype: bool
        """
        if arra is None or len(arra) <= 0:
            return False
        # 转换A J Q K为对应的数字
        trans_dict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(arra)):
            if arra[i] in trans_dict.keys():
                key = arra[i]
                arra[i] = trans_dict[key]

        num_gaps = 0
        num_zeros = 0
        # 对arra进行排序
        arra = sorted(arra)

        #  统计数组中0的个数
        for i in arra:
            if i == 0:
                num_zeros += 1


        # 统计间隔的数目
        small = num_zeros # 排序以后，从0以后开始
        big = small + 1
        while big < len(arra):
            # 当两个数相等时，则说明有对子，不可能是顺子
            if arra[small] == arra[big]:
                return  False
            num_gaps += arra[big] - arra[small] - 1
            small = big
            big += 1
        return False if num_gaps > num_zeros else True

if __name__ == "__main__":
    s = Solution()
    test1 = ['A', 3, 2, 5, 0]
    test2 = [0, 3, 1, 6, 4]
    print(s.isContinuous(test1))
    print(s.isContinuous(test2))

