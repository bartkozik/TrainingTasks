def diagonal_difference(arr, n):
    count = 0
    sum1 = 0
    sum2 = 0
    j1 = 0
    j2 = n - 1
    while count < n:
        sum1 = sum1 + arr[count][j1]
        sum2 = sum2 + arr[count][j2]
        count += 1
        j1 += 1
        j2 -= 1
    return abs(sum1 - sum2)
