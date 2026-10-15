def matrixMedian(matrix):
    arr = sorted(x for row in matrix for x in row)
    return arr[len(arr) // 2]
