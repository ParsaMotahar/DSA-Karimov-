'''Rotate Matrix/ Image - LeetCode 48

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

Example:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

import numpy as np
def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            '''The second for loops start at i because this
            ensures that we skip over the cells that
            has already been flipped'''
            
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

matrix = transpose(matrix)
matrix = np.flip(matrix, 1)
print(matrix)