def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print()
def flip(matrix):
    matrixB = []
    r = len(matrix)
    for i in range(r-1,-1,-1):
        matrixB.append(matrix[i])
    return matrixB

m1 = [[1,4],
      [2,5],
      [3,6]]
m2 = flip(m1)
printMatrix(m1)

printMatrix(m2)
