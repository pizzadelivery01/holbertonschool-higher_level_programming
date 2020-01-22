#!/usr/bin/python3


def pascal_triangle(n):
    """
    gets pascal triangle for n line,
    """


    matrix = []
    for i in range(0, n):
        matrixlen = len(matrix)
        if matrixlen <= 1:
            matrix.append([1 for each in range(0, mat_len + 1)])
        else:
            row = []
            for j in range(0, len(matrix[i - 1]) + 1):
                if j == 0 or j == len(matrix[i - 1]):
                    row.append(1)
                else:
                    row.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
            matrix.append(row)
    return matrix
