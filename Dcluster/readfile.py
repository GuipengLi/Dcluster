import numpy as np

def readfile(file, dimensions = 2,sep=' '):
    '''
    Input file format: 3 columns ,seperated by ' '
    Column 1: element1
    Column 2: element2
    Column 3: distance between element1 and element2
    For example: (id > 0)
        1   2   0.6
        1   3   2.3
        2   3   1.4
    Return (dist,xxdist,ND,N)
    '''
    print('Loading the file ...')
    xx = np.genfromtxt(file, delimiter=sep,names=['x','y','dist'],dtype="i8,i8,f8")
    # ND: number of data point
    X = xx['x']
    Y = xx['y']
    xxdist = xx['dist']
    ND = Y.max()
    NL = X.max()
    if NL>ND:
        ND = NL
    # N: number of point pairs/distance
    N = xx.shape[0]
    dist = np.zeros((ND,ND))

    # dist may save half of memory
    for i in range(N):
        ii = X[i]-1
        jj = Y[i]-1
        dist[ii,jj] = xxdist[i]
        dist[jj,ii] = xxdist[i]

    return((dist,xxdist,ND,N))
