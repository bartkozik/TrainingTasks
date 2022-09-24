def minimumBribes(q):
    # Write your code here
    bribes = 0
    for num in q:
        if 0 < num - q.index(num)-1 <=2:
            bribes+=num - q.index(num)-1
        elif num - q.index(num)-1 > 2:
            print('Too chaotic')
        else:
            bribes+=0
    #print(bribes)


q = [2,1,5,3,4]
s = [2,5,1,3,4]
print(minimumBribes(q))
print(minimumBribes(s))

for num in q:
    if 0 < num - q.index(num) - 1 < 3:
        bribes += num - q.index(num) - 1

    elif num - q.index(num) - 1 >= 3:
        print('Too chaotic')
        return
    else:
        bribes += 0
print(bribes)