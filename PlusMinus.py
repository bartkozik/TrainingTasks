def plus_minus(arr):
    zeros = 0
    negatives = 0
    positives = 0
    for num in arr:
        if num == 0:
            zeros += 1
        elif num < 0:
            negatives += 1
        else:
            positives += 1
    prop_neg = negatives / len(arr)
    prop_pos = positives / len(arr)
    prop_zer = zeros / len(arr)
    print("{:.5f}".format(prop_pos))
    print("{:.5f}".format(prop_neg))
    print("{:.5f}".format(prop_zer))
