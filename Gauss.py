import numpy as np

m = np.matrix('0 0 -2 0 7 12;2 4 -10 6 12 28; 2 4 -5 6 -5 -1')


print(m)

#todo check no solution in case of 2 all zero rows (one of which indicates no solution)

def MainMethod(m):
    #Preparing augmented matrix
    m = m.astype(float)
    m = remove_0col(m)
    #running Gaussian Elimination
    m = GaussianElimination(m)
    print(m)
    #checking if there is a solution
    if True == NoSolution(m):
        print("There is no solution to the system")
    else:
        m = ReducedRowEchelonForm(m)
        print(m)

def GaussianElimination(m):
    emptycol = step1(m)
    m = step2(m,emptycol)
    m = step3(m,emptycol)
    m = step4(m,emptycol)
    #step5 (recursive call on a submatrix)
    a, b = m.shape
    if a > 1 and b > 1:
        m[1:,1:] = GaussianElimination(m[1:,1:])
    return m


def ReducedRowEchelonForm(m):
    a, b = m.shape
    for i in range(a - 1, 0, -1):
        if np.count_nonzero(m[i, :]) == 0:
            continue  # continue if row doesn't add any information (it contains all zeros)
        for k in range(0, b - 1):
            if m[i, k] == 0:
                continue
            if m[i, k] != 1:
                print("Error: Matrix is not in Row-echelon-Form")
            if m[i, k] == 1:
                # make all numbers above zero
                for j in range(i - 1, -1, -1):
                    if m[j, k] == 0:
                        continue
                    else:
                        RowAddition(m, j, i, (-1 * m[j, k]))
                break

    return m

def PrintSolution(m):
    d = dict()
    a,b = m.shape
    for i in range(a-1,-1,-1):
        d2 = dict()

        check = 0
        if np.count_nonzero(m[i, :]) == 0:
            continue
        for k in range(0, b - 1):
            if m[i, k] == 0:
                continue
            if m[i,k] != 0 and len(d2) > 0:
                xsubscript =str(k+1)
                d2[k+1] == "-x"+xsubscript

            if m[i, k] == 1 and len(d2) == 0:
                check = k+1
        d[check] == m[i, b - 1]


    # save first 1
    #loop through rest of line to see if empty, each one is saved in dict and in a line count dict
    #print first 1 = m[i,b-1] + whatever is in the overall dict for where the line count dict > 0
    #add first 1 to overall dict
    #move to above line
    #


    #from buttom up
    #have array of arbitrary numbers and an incrementer

    #look at col number of leading 1 to determine suffix of x


def remove_0col(m):
    zeroCol = []
    for i in range(0,m[0,:].size-1):
        if m[:,i].sum() == 0:
            zeroCol.append(i)
    m = np.delete(m, zeroCol, axis=1)
    if zeroCol.__len__() > 0:
        print("The columns" + zeroCol.__str__() + "Have been removed, since all the unknown variables have the constant weight of 0")
    return m


def step1(m):
    emptycol = 0
    while np.count_nonzero(m[:,emptycol]) == 0:
        emptycol += 1
    return emptycol

def step2(m,emptycol):

    if m[0,emptycol] != 0:
        return m
    else:
        k = 0
        for i in m[:,emptycol]:
            if i !=0:
                RowSwap(m,0,k)
                return m
            k+=1
    return m

def step3(m,emptycol):
    if m[0,emptycol] == 1:
        return m
    n = 1/m[0,emptycol]
    m = RowMultiply(m,0,n)
    return m

def step4(m,emptycol):
    k=1
    newM = m
    for i in m[1:,emptycol]:
        if i != 0:
            n = -i
            newM = RowAddition(newM,k,0,n)
        k+=1
    return newM


def NoSolution(m):
    a,b = m.shape
    if 0 == np.count_nonzero(m[a-1,0:b-1]):
        if m[a - 1, b - 1] != 0:
            return True
    return False


def RowSwap(m,r1,r2):
    m[[r1,r2]] = m[[r2,r1]]
    return m
def RowMultiply(m,r,n):
    #m is a matrix, r1 is the row, n is the number to multiply with
    m[r] = m[r]*n
    return m
def RowAddition(m,r1,r2,n):
    #multiplies a row, r1, with another row, r2, times some constant n.
    m[r1]  = m[r1]+n*m[r2]
    return m

MainMethod(m)
