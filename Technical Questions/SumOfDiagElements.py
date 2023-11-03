'''Given 2D list calculate the sum of diagonal elements.

Example

    myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
     
    diagonal_sum(myList2D) # 15'''

import numpy as np
arr = np.array([[1,2,3,4],[4,5,6,8], [9,10,11,12], [13,14,15,16],[17,18,19,20]])
print(arr, end="\n\n")
def diagonal_sum(arr):
    c = 0
    sum = 0
    for r in range(len(arr)):
        try:
            sum += arr[r][c]
            c += 1
        except:
            break

        '''note that the try and the except
        statement is just an easy fix to errors
        happening as a result of a not square matrix'''

    return sum
print(diagonal_sum(arr))