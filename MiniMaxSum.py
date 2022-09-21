def miniMaxSum(arr):
    new_arr=sorted(arr)
    minimum = sum(new_arr[0:4])
    maximum = sum(new_arr[1:5])
    print(minimum, maximum )