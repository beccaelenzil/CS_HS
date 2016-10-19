def fibIter(n):
    fibSeq = [0,1]
    if n <= 1:
        return 1
    else:
        for i in range(2,n):
            fibSeq.append(fibSeq[i-1] + fibSeq[i-2])
            print fibSeq
        return fibSeq[n-1]
print fibIter(9)
