def flippingMatrix(matrix):
    sum_up = 0
    for i in range(n):
        for j in range(n):
            list = [matrix[i][j], matrix[i][2 * n - 1 - j], matrix[2 * n - 1 - i][j],
                    matrix[2 * n - 1 - i][2 * n - 1 - j]]
            sum_up += max(list)
    return sum_up


