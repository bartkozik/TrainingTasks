q = int(input())
enqueue = []
dequeue = []

for i in range(q):
    t = list(input().split())
    if t[0] == '1':
        enqueue.append(t[1])

    elif t[0] == '2':
        if not dequeue:
            while enqueue:
                dequeue.append(enqueue.pop())
        dequeue.pop()
    else:
        if not dequeue:
            while enqueue:
                dequeue.append(enqueue.pop())
        print(dequeue[-1])

        
