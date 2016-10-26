#https://trinket.io/library/trinkets/df0a6385e7
def fibIter(n):
    fibSeq = [0,1]
    if n <= 1:
        return 1
    else:
        for i in range(2,n):
            fibSeq.append(fibSeq[i-1] + fibSeq[i-2])
        return fibSeq[n-1]
#print fibIter(9)
def fibRecurse(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibRecurse(n-1) + fibRecurse(n-2)
#print fibRecurse(9)
def listReverse(l):
    list = range(len(l))
    start = -1
    for i in l:
        list[start] = i
        start += - 1
    return list

def listReverseIter(l):
    if len(l) == 1:
        return l
    else:
        return listReverseIter(l[1:])+[l[0]]
# List Reverse Tests
#print "listReverse([1,2,3,4]) == [4,3,2,1] = ",listReverse([1,2,3,4])," : ",listReverse([1,2,3,4]) == [4,3,2,1]
#print "listReverseIter([1,2,3,4]) == [4,3,2,1] = ",listReverseIter([1,2,3,4])," : ",listReverseIter([1,2,3,4]) == [4,3,2,1]
