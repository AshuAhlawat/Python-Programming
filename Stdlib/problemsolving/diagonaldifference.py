import math
import random

def diagonaldifference(arr):
    first_diagonal_sum = 0
    for i in range(len(arr[0])):
        first_diagonal_sum += arr[i][i]
    
    second_diagonal_sum = 0
    j = -1
    for i in range(len(arr[0])):
        second_diagonal_sum += arr[i][j]
        j -= 1
    result = abs(first_diagonal_sum - second_diagonal_sum)
    print(result)

a = [[11,2,4],[4,5,6],[10,8,-12]]
diagonaldifference(a)