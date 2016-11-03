# python 2
#
# Game of Life
#
# Name:
#

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A.append(createOneRow(width))
    return A
def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line
def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A
def innerCells(w,h):
    '''
    creates an empty board and modifies it so all but the boarders are on
    '''
    A = createBoard(w,h)
    for row in range(h):
        if row == 0 or row == h-1:
            for col in range(w):
                A[row][col] = 0
        else:
            for col in range(w):
                if col == 0 or col == w-1:
                    A[row][col] = 0
                else:
                    A[row][col] = 1
    return A

def randomCells(w,h):
    '''
    creates an empty board and modifies it so all boarders are off, and all inners are randomly either on or off
    '''
    A = createBoard(w,h)
    for row in range(h):
        if row == 0 or row == h-1:
            for col in range(w):
                A[row][col] = 0
        else:
            for col in range(w):
                if col == 0 or col == w-1:
                    A[row][col] = 0
                else:
                    A[row][col] = random.choice([0,1])
    return A
def copy(A):
    copy = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        copy.append([])
        for col in range(w):
            copy[row].append(A[row][col])
    return copy
def innerReverse(A):
    reverse = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        reverse.append([])
        for col in range(w):
            if row == 0 or row == h-1 or col == 0 or col == w-1:
                reverse[row].append(0)
            else:
                reverse[row].append((A[row][col]+1)%2)
    return reverse
def countNeighboroughs(row,col,A):
    a = A[row][col]
    counter = 0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if r == row and c == col:
                pass
            elif A[r][c] == 1:
                counter += 1
            else:
                pass
    return counter

def next_life_generation(A):
    neigh = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        neigh.append([])
        for col in range(w):
            if row == 0 or row == h-1 or col == 0 or col == w-1:
                neigh[row].append(0)
            else:
                neigh[row].append(countNeighboroughs(row,col,A))
    newA = []
    for row in range(h):
        newA.append([])
        for col in range(w):
            if row == 0 or row == h-1 or col == 0 or col == w-1:
                newA.append(0)
            else:
                if neigh[row][col] < 2 or neigh[row][col] >3:
                    newA[row].append(0)
                elif neigh[row][col] == 3:
                    newA[row].append(1)
                else:
                    newA[row].append(A[row][col])
    return newA
A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
printBoard(A)
A2 = next_life_generation(A)
printBoard(A2)
A3 = next_life_generation(A2)
printBoard(A3)

