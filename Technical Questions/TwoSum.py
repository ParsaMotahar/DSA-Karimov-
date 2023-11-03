import numpy as np
arr = np.array([2,6,3,9,11,0,2,5,3,7,2,1,2,3,4,5,6])
def TwoSum(arr, target):
    solutionArray = []
    for i in arr:
        if (target - i) in arr and target - i not in solutionArray:
            solutionArray.append(i)
            solutionArray.append(target-i)
        else:
            continue
    return solutionArray
print(TwoSum(arr, 9))