import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def rhodelta(dist, xxdist, ND, N, percent = 2.0):
    '''
    Input file format: 3 columns ,seperated by ' '
    Return (rho,delta,ordrho)
    '''
    print('Caculating rho and delta...')
    print('average percentage of neighbours (hard coded): %5.6f'%(percent) )

    position = round(N*percent/100)
    sda=np.sort(xxdist)
    dc=sda[position]
    print('Computing Rho with gaussian kernel of radius: %12.6f\n'%(dc))

    rho = np.zeros(ND)
    # Gaussian kernel
    for i in range(ND-1):
        for j in range((i+1),ND):
            rho[i] = rho[i] + np.exp(-(dist[i,j]/dc)*(dist[i,j]/dc))
            rho[j] = rho[j] + np.exp(-(dist[i,j]/dc)*(dist[i,j]/dc))

    maxd = dist.max()
    ordrho = (-rho).argsort()
    delta = np.zeros(ND)
    nneigh = np.zeros(ND)
    delta[ordrho[0]] = -1
    nneigh[ordrho[0]] = 0

    for ii in range(1,ND):
        delta[ordrho[ii]] = maxd
        for jj in range(ii):
            if dist[ordrho[ii],ordrho[jj]]<delta[ordrho[ii]]:
                delta[ordrho[ii]] = dist[ordrho[ii],ordrho[jj]]
                nneigh[ordrho[ii]] = ordrho[jj]

    delta[ordrho[0]] = delta.max()
    print('Generated file:DECISION GRAPH')
    print('column 1:Density')
    print('column 2:Delta\n')
    dg = np.array([rho,delta]).T
    np.savetxt('DECISION_GRAPH.txt',dg,fmt='%.4f')
    return((rho,delta,ordrho,dc,nneigh))
