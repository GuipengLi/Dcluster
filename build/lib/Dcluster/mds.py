import numpy as np
from numpy.linalg import *

def mds(d, dimensions = 2):
    """
    Multidimensional Scaling - Given a matrix of interpoint distances,
    find a set of low dimensional points that have similar interpoint
    distances.
    """
    print('Multidimensional Scaling for scatter plot...')
    (n,n) = d.shape
    E = (-0.5 * d**2)
    # Use mat to get column and row means to act as column and row means.
    Er = np.mat(np.mean(E,1))
    Es = np.mat(np.mean(E,0))
    F = np.array(E - np.transpose(Er) - Es + np.mean(E))
    [U, S, V] = svd(F)
    Y = U * np.sqrt(S)
    return (Y[:,0:dimensions], S)
