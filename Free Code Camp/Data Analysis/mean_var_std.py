import numpy as np


def calculate(list):
    print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
    calculations = {}
    ## min, max,
    rowL = []
    npMatrixList = []
    for l in list:
      rowL.append(l)
      if len(rowL) == 3:
        npMatrixList.append(rowL)
        rowL = []

    npMatrix = np.matrix(npMatrixList)
    
    #axis1 are rows
    #axis 2 are columns 
    flattenSum = np.sum(list)

    axis1sum = np.sum(npMatrix, axis = 0) 
    
    axis2sum = np.sum(npMatrix, axis = 1) 
    
    sumDict = [axis1sum, axis2sum, flattenSum]
    calculations['sum'] = sumDict




    return calculations