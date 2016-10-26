def fibIter(n):
    fibSeq = [0,1]
    if n <= 1:
        return 1
    else:
        for i in range(2,n):
            fibSeq.append(fibSeq[i-1] + fibSeq[i-2])
        return fibSeq[n-1]
print fibIter(9)
def fibRecurse(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibRecurse(n-1) + fibRecurse(n-2)
print fibRecurse(9)
