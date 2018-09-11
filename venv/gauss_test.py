import numpy as np

m = np.matrix('0 1 2 2 -3;0 0 1 -2 -2;0 0 0 1 1')
print(m)
#print(m[0,:].size)
def RowAddition(m,r1,r2,n):
    #multiplies a row, r1, with another row, r2, times some constant n.
    m[r1]  = m[r1]+n*m[r2]
    return m

def ReducedRowEchelonForm(m):
    a,b = m.shape
    for i in range(a-1,0,-1):
        if np.count_nonzero(m[i,:]) == 0:
            continue #continue if row doesn't add any information (it contains all zeros)
        for k in range(0,b-1):
            if m[i,k] == 0:
                continue
            if m[i,k] != 1:
                print("Error: Matrix is not in Row-echelon-Form")
            if m[i,k] == 1:
                #make all numbers above zero
                for j in range(i-1,-1,-1):
                    if m[j,k] == 0:
                        continue
                    else:
                        RowAddition(m,j,i,(-1*m[j,k]))

                    
                
                #times -1 
                #all rows, continue at current
    return m
ReducedRowEchelonForm(m)




#NoSolution(m)
"""

def NoSolution(m):
    a,b = m.shape
    if 0 == np.count_nonzero(m[a-1,0:b-1]):
        if m[a - 1, b - 1] != 0:
            return True
    return False
"""