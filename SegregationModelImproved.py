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
    ''' prints board in grid form'''
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

def randomCells(w,h,type1,type2,typestore):
    '''
    creates an empty board and modifies it so all boarders are off, and all inners are randomly either on or off
    '''
    total = (w-2)*(h-2)
    t1 = total * type1
    t2 = total * type2
    t3 = total * typestore
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
                        elif num < t1+t2+t3:
                            A[row][col] = 3
                            t3 += -1
                        else:
                            A[row][col] = 0
                        total += -1
    return A

def countNeighboroughs(row,col,A):
    '''returns [number of type 1 of the surrounding 8,number of type 2, type of tile referenced
    by coordinates (row,col) in grid A'''
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
    '''creates a list of coordinates of empty cells in A'''
    empties = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            if A[row][col] == 0:
                empties.append([row,col])
    return empties
def countNeighboroughsArray(A):
    '''creates an array where the countneighboroughs list is in the place of the value of each cell'''
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
def vacateList(A,thresh,storeradius,storethresh):
    '''creates a list of the cells that need to leave based on the rules:
    If the proportion of neighboroughs that are similar is less than Thresh,
    Or the cell is type 3, and proportion of cells within storeradius cells is below storethresh,
    or the cell is occupied non-type 3, and there isn't a type 3 cell within storeradius cells'''
    neigh = countNeighboroughsArray(A)
    vacaters = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            if A[row][col] == -1 or A[row][col] == 0:
                pass
            else:
                totalnumneighboroughs = neigh[row][col][0] + neigh[row][col][1]
                mynumneighboroughs = neigh[row][col][neigh[row][col][2]-1]
                if totalnumneighboroughs > 0 and float(mynumneighboroughs)/totalnumneighboroughs < thresh and A[row][col] > 0:
                    vacaters.append([row,col])
                elif A[row][col] == 1 or A[row][col] == 2:
                    if bigcountneighboroughs(storeradius,row,col,A)[0] < 1:
                        vacaters.append([row,col])
                elif A[row][col] == 3:
                    if bigcountneighboroughs(storeradius,row,col,A)[1] < storethresh:
                        vacaters.append([row,col])
    return vacaters
def bigcountneighboroughs(r,row,col,A):
    '''returns [number of stores within r cells, number of occupied cells within r cells'''
    neigh = [0,0]
    h = len(A)
    w = len(A[0])
    [xstart,xend,ystart,yend] = [col-r,col+r+1,row-r,row+r+1]
    while xstart < 0:
        xstart +=1
    while ystart < 0:
        ystart +=1
    while xend > w-1:
        xend += -1
    while yend > h-1:
        yend += -1
    for y in range(ystart,yend):
        for x in range(xstart,xend):
            if y == row and x == col or A[y][x] == -1:
                pass
            else:
                if  A[y][x] == 1 or A[y][x] == 2:
                    neigh[1] += 1
                elif A[y][x] == 3:
                    neigh[0] += 1
    return neigh
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
def next_life_generation(A,thresh,storeradius,storethresh):
    '''cretes the next generation grid, moving random cells from the vacater list and placing
    them in empty coordinates. does not place if either vacater or empties list is empty'''
    empties = listempties(A)
    vacaters = vacateList(A,thresh,storeradius,storethresh)
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
def nextlifegenStat(A,thresh,storeradius,storethresh):
    '''does the same as nextlifegeneration, but returns as list [A,0] if the simulation is static'''
    empties = listempties(A)
    vacaters = vacateList(A,thresh,storeradius,storethresh)
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
def main(radius):
    '''returns the segregation index after 110 generations for 90 different scenarios, taking the average
    of gens 101-110, or the final value if the simulation goes static earlier, in a grid form.
    rows are threshhold values - multiples of 5 from 0 to 75. columns are store proportion threshholds
    - multiples of 4 from 0 to 24'''
    data = []
    for thresh in range(15):
        data.append([])
        for storeprop in range(6):
            print ['a',thresh,storeprop]
            A = randomCells(50,50,.35,.35,float(4)*storeprop/100)
            c = 0
            d = 0
            e = 0
            ave = []
            while len(A) > 2:
                print c
                if c > 100:
                    d += 1
                    ave.append(segregationIndex(A))
                    if d == 10:
                        data[thresh].append(sum(ave)/len(ave))
                        e = 1
                        break
                A = nextlifegenStat(A,float(5)*thresh/100,4,(2*radius)*(2*radius-1.5))
                c += 1
            if e == 0:
                data[thresh].append(segregationIndex(A[0]))
    return data
def toexcel():
    '''places grids formed in main function into excel spreadsheets. makes 5 sheets,
    one for each value of store radius 1-5'''
    wb = openpyxl.load_workbook('grid.xlsx')
    for i in range(5):
        print i,'sheet'
        wb.save('grid.xlsx')
        data = main(i+1)
        sheet = wb.get_sheet_by_name('Sheet'+str(i+1))
        for row in range(len(data)):
            for col in range(len(data[0])):
                print [row,col]
                sheet.cell(column=col+1,row=row+1).value=data[row][col]
    wb.save('grid.xlsx')
toexcel()
