#https://trinket.io/library/trinkets/df0a6385e7
def listreverse(l):
    list = range(len(l))
    start = -1
    for i in l:
        l[start] = i + 
        start = start - 1
    return list

def listreverseIter(l):
    list = []
    if len(list) == len(l):
        return list
    else:
        listreverseIter(l[0:-1])
# List Reverse Tests
print "listReverse([1,2,3,4]) == [4,3,2,1] = ",listreverse([1,2,3,4])," : ",listreverse([1,2,3,4]) == [4,3,2,1]
print "listReverseIter([1,2,3,4]) == [4,3,2,1] = ",listreverseIter([1,2,3,4])," : ",listreverseIter([1,2,3,4]) == [4,3,2,1]
