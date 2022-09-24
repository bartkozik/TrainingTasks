def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i in range(len(q)-1,0,-1):
        if q[i]!= i+1:
            if q[i-1] == i+1:
                bribes+=1
                q[i-1],q[i]=q[i],q[i-1]
            elif q[i-2] == i+1:
                bribes+=2
                q[i-2],q[i-1],q[i]=q[i-1],q[i],q[i-2]
            else:
                print('Too chaotic')
                return
    print(bribes)