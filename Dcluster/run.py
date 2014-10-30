# -*- coding: utf-8 -*-
import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from .mds import mds
from .readfile import readfile
from .rhodelta import rhodelta
from .DCplot import DCplot

def run(*args, **kwargs):
    '''
    return cluster id
    '''
    file = kwargs.get('fi')
    sep = kwargs.get('sep',' ')
    ########
    (dist,xxdist,ND,N) = readfile(file, dimensions = 2, sep=sep)
    XY, eigs = mds(dist)
    (rho,delta,ordrho,dc,nneigh) = rhodelta(dist, xxdist, ND, N, percent = 2.0)
    DCplot(dist, XY, ND, rho, delta,ordrho,dc,nneigh,17,0.1)



