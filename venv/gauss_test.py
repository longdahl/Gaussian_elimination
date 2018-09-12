import numpy as np

m = np.matrix('0 1 2 2 -3;0 0 1 -2 -2;0 0 0 1 1')
print(m)
#print(m[0,:].size)
def dicttest():
    d = dict()
    print(len(d))
dicttest()




#NoSolution(m)
"""

def NoSolution(m):
    a,b = m.shape
    if 0 == np.count_nonzero(m[a-1,0:b-1]):
        if m[a - 1, b - 1] != 0:
            return True
    return False
"""