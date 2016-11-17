import random
import openpyxl
def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A.append(createOneRow(width))
    return A

def randomCells(w,h,type1,type2):
    '''
    creates an empty board and modifies it so all boarders are off, and all inners are randomly either on or off
    '''
    total = (w-2)*(h-2)
    t1 = total * type1
    t2 = total * type2
    A = createBoard(w,h)
    for row in range(h):
            for col in range(w):
                    if row == 0 or row == h-1 or col == 0 or col == w-1:
                        A[row][col] = -1
                    else:
                        num = random.randint(0,total)
                        if num < t1:
                            A[row][col] = 1
                            t1 += -1
                        elif num < t1+t2:
                            A[row][col] = 2
                            t2 += -1
                        else:
                            A[row][col] = 0
                        total += -1
    return A

def countNeighboroughs(row,col,A):
    list = [0,0,0]
    list[-1] = A[row][col]
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if r == row and c == col or A[r][c] == -1:
                pass
            elif A[r][c] == 1:
                list[0] += 1
            elif A[r][c] == 2:
                list[1] += 1
            else:
                pass
    return list
def listempties(A):
    empties = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            if A[row][col] == 0:
                empties.append([row,col])
    return empties
def countNeighboroughsArray(A):
    neigh = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        neigh.append([])
        for col in range(w):
            if A[row][col] == -1:
                neigh[row].append(-1)
            else:
                neigh[row].append(countNeighboroughs(row,col,A))
    return neigh
def vacateList(A,thresh):
    neigh = countNeighboroughsArray(A)
    vacaters = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            if A[row][col] == -1:
                pass
            else:
                totalnumneighboroughs = neigh[row][col][0] + neigh[row][col][1]
                mynumneighboroughs = neigh[row][col][neigh[row][col][2]-1]
                if totalnumneighboroughs > 0:
                    if float(mynumneighboroughs)/totalnumneighboroughs < thresh and A[row][col] > 0:
                        vacaters.append([row,col])
    return vacaters
def next_life_generation(A,thresh):
    empties = listempties(A)
    vacaters = vacateList(A,thresh)
    if len(vacaters) == 0:
        return [A,0]
    else:
        emptiescopy = empties
        vacaterscopy = vacaters
        h = len(A)
        w = len(A[0])
        changes = [[],[]]
        for i in range(len(vacaterscopy)):
            if len(emptiescopy) > 0:
                start = random.randint(0,len(vacaterscopy)-1)
                finish = random.randint(0,len(emptiescopy)-1)
                changes[0].append(vacaterscopy[start])
                changes[1].append(emptiescopy[finish])
                vacaterscopy.remove(vacaterscopy[start])
                emptiescopy.remove(emptiescopy[finish])
        newA = []
        for row in range(h):
            newA.append([])
            for col in range(w):
                if [row,col] in changes[0]:
                    newA[row].append(0)
                elif [row,col] in changes[1]:
                    oldvaluecoord = changes[0][changes[1].index([row,col])]
                    oldvalue = A[oldvaluecoord[0]][oldvaluecoord[1]]
                    newA[row].append(oldvalue)
                else:
                    newA[row].append(A[row][col])
        return newA
def copy(A):
    '''makes a copy of A'''
    copy = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        copy.append([])
        for col in range(w):
            copy[row].append(A[row][col])
    return copy
def segregationIndex(A):
    '''returns th average proportion of neighboroughs that are friendly, across the
    entire board'''
    neigh = countNeighboroughsArray(A)
    height = len(A)
    width = len(A[0])
    segregation = copy(A)
    segregationList = []
    for row in range(height):
        for col in range(width):
            if A[row][col] == 1 or A[row][col] == 2:
                totalneighboroughs = neigh[row][col][0] + neigh[row][col][1]
                sameneighboroughs = neigh[row][col][neigh[row][col][2]-1]
                if totalneighboroughs > 0:
                    segregation[row][col] = float(sameneighboroughs)/float(totalneighboroughs)
                    segregationList.append(segregation[row][col])

    # take the average of the segregationIndex for each cell to get a single metric
    segregationTotal = sum(segregationList)/len(segregationList)
    return segregationTotal
def main():
    '''returns the segregation index after 110 generations for 90 different scenarios, taking the average
    of gens 101-110, or the final value if the simulation goes static earlier, in a grid form.
    rows are threshhold values - multiples of 5 from 0 to 75. columns are store proportion threshholds
    - multiples of 4 from 0 to 24'''
    data = []
    for thresh in range(15):
        A = randomCells(50,50,.35,.35)
        c = 0
        d = 0
        e = 0
        list = []
        while len(A) != 2:
            if c > 100:
                d += 1
                list.append(segregationIndex(A))
                if d == 10:
                    e = 1
                    data.append(sum(list)/len(list))
                    break
            A = next_life_generation(A,float(5)*thresh/100)
            c += 1
        if e == 0:
            data.append(segregationIndex(A[0]))
    return data
def toexcel():
    '''places list made in main function into excel'''
    wb = openpyxl.load_workbook('grid1.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    data = main()
    for col in range(len(data)):
        sheet.cell(column=col+1,row=2).value=data[col]
    wb.save('grid1.xlsx')
toexcel()
