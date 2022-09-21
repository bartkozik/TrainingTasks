def find_median(arr):
    new_arr = sorted(arr)
    if len(new_arr) % 2 != 0:
        return new_arr[len(arr) // 2]
    else:
        return (new_arr[len(arr) / 2] + new_arr[len(arr) / 2 - 1]) / 2
