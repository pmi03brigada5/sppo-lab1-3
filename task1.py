import numpy as np
n = 3
matrix = np.zeros(shape=(n, n))
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())
vector = np.zeros(shape=n)
for i in range(n):
    vector[i] = int(input())
print("Матрица:\n", matrix)
print("Вектор:\n", vector)

matrix = matrix.transpose()
print("Транспонированная матрица:\n", matrix)
result = np.matmul(matrix, vector)
print("Вектор с решениями уравнения:\n", result)