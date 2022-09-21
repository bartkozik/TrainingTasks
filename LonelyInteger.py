from collections import Counter

def lonelyinteger(a):
    #counted = {}
    #for num in a:
        #if num not in counted:
            #counted[num]=1
        #else:
            #counted[num]+=1
    counted = Counter(a)
    for key,val in counted.items():
        if counted[key] == 1:
            return key