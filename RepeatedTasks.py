def power(b,p):
    if b == 0 and p == 0:
        return 1
    start = b
    for x in range(1,p):
        b = b*start
    return b
print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)
def summedOdds(L):
    result = 0
    for x in L:
        if x%2 == 1:
            result = result + x
    return result
print "summedOdds( [4,5,6] ): should be 5 == ", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be 24 == ", summedOdds( range(3,10) )
def mult(n,m):
    start = n
    if m > 0:
        for x in range(1,m):
            n = n + start
        return n
    if m == 0:
        return 0
    if m < 0:
        for x in range(m,-1):
            n = n + start
        return -n
print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)

def dot(k,l):
    if len(k) != len(l):
        return 0
    else:
        result = 0
        for x in range(0,len(k)):
            result = result + k[x]*l[x]
        return result
print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] )
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] )
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] )
print "dot( [], [6] )           0.0 ==", dot( [], [6] )
print "dot( [], [] )            0.0 ==", dot( [], [] )

def count_evens(L):
    n = 0
    for x in L:
        if x%2 == 0:
            n = n + 1
    return n
print "count_evens([2, 1, 2, 3, 4], 3 == ", count_evens([2, 1, 2, 3, 4])
print "count_evens([2, 2, 0]), 3 == ", count_evens([2, 2, 0])
print "count_evens([1, 3, 5]), 0 == ", count_evens([1, 3, 5])

def count9(L):
    n = 0
    for x in L:
        if x == 9:
            n = n + 1
    return n
print "count9([1, 2, 9]), 1 == ",count9([1, 2, 9])
print "count9([1, 9, 9]), 2 == ",count9([1, 9, 9])
print "count9([1, 9, 9, 3, 9]), 3 == ",count9([1, 9, 9, 3, 9])

def printrect(width,height,symbol):
    L =''
    for x in range(0,width):
        L = L + symbol
    for h in range(0,height):
        print L
printrect(4,6,'%')

def printtriangle(width, symbol,rightsideup):
    L = ''
    if rightsideup == True:
        for x in range(1,width+1):
            print symbol*x
    if rightsideup == False:
        for x in range(width,0,-1):
            print symbol*x
printtriangle(3,'@',True)
printtriangle(3,'$',False)
def printbumps(num,symbol1,symbol2):
    for x in range(0,num+1):
        printtriangle(x,symbol1,True)
        printtriangle(x,symbol2,False)
printbumps(3,'&','!')



def uniq( L ):
    """ returns whether all elements in L are unique
          input: L, a list of any elements
          output: True, if all elements in L are unique,
               or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return uniq( L[1:] ) # recursion is OK, too!
def untilarepeat(high):
    import random
    n = 0
    L = []
    while uniq(L) == False:
        L = L + random.choice(range(0,high))
        n = n + 1
    return n
