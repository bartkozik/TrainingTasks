def superDigit(n, k):
    # Write your code here
    n_arr = list(n.strip(' '))
    n_ints = sum([int(x) for x in n_arr])
    count = n_ints * k
    while count > 10:
        super_num = 0
        for num in str(count):
            super_num += int(num)
        count = super_num
    return count
