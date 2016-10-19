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
    currentPosition = start
    counter
    if currentPosition >= hi or currentPosition <= lo:
        return counter
