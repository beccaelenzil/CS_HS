import random

def rs():
    return random.choice([-1,1])
def rwPos(start,nsteps):
    currentPosition = start
    for i in range(0,nsteps):
        currentPosition = currentPosition + rs()
        print 'current position is' + str(currentPosition)
    return currentPosition

def rwsteps(start,lo,hi):
    counter = 0
    currentPosition = start
    while currentPosition < hi and currentPosition > lo:
        counter += 1
        startspace = ' '*(currentPosition-lo-1)
        endspace = ' '*(hi-currentPosition-1)
        print '|'+startspace+'S'+endspace+'|',currentPosition
        currentPosition += rs()
    print 'It took', counter,'times'

rwsteps(5,0,10)
