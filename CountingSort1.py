def countingSort(arr):
    freq_arr = [0] * 100
    for i in range(0, len(arr)):
        if freq_arr[arr[i]] == 0:
            freq_arr[arr[i]] = 1
        else:
            freq_arr[arr[i]] += 1
    return freq_arr
