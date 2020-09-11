#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 矩阵中的路径.py
@time: 2020/02/18

"""
'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 [[a b c e], [s f c s], [a d e e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """
        :param matrix:  二维矩阵
        :param rows:    二维矩阵的行数
        :param cols:    二维矩阵的列数
        :param path:    目标路径
        :return:        是否包含目标路径
        """
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return  False
        visited = [0]*(rows*cols)
        path_length = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, path_length, visited):
                    return  True
        return  False


    def hasPathCore(self, matrix, rows, cols, row, col, path, path_length, visited):
        """
        :param matrix:  二维矩阵
        :param rows:    二维矩阵的行数
        :param cols:    二维矩阵的列数
        :param row:     当前访问坐标的行
        :param col:     当前访问坐标的列
        :param path:    目标路径
        :param path_length:  访问路径的长度
        :param visited:      字符布尔矩阵，表示当前格子是否被访问
        :return:  当前格子是否应该在路径中
        """
        if len(path) == path_length:
            return  True
        has_path = False
        if row >= 0 and row < rows and \
            col >= 0 and col < cols and \
            matrix[row*cols + col] == path[path_length] and \
            not visited[row*cols + col]:
            path_length += 1
            #print(path_length)
            visited[row*cols + col] = True
            has_path = self.hasPathCore(matrix, rows, cols, row, col - 1, path, path_length, visited) or\
                       self.hasPathCore(matrix, rows, cols, row, col + 1, path, path_length, visited) or\
                       self.hasPathCore(matrix, rows, cols, row - 1, col, path, path_length, visited) or \
                       self.hasPathCore(matrix, rows, cols, row + 1, col, path, path_length, visited)

            if not  has_path:
                path_length -= 1
                visited[row*cols + col] = False
        return  has_path


if __name__ == "__main__":
    s = Solution()
    #ifTrue1 = s.hasPath("ABCESFCSADEE", 3, 4, "ABCCEDE")
    ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
    print(ifTrue2)