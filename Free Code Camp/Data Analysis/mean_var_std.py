import numpy as np


def calculate(list):
    # if len(list) != 9:
    #   return "Throw exception"
    #First convert list to np.array 
    npArr = np.array(list)

    meanRows = [npArr[[0,1,2]].mean(), npArr[[3,4,5]].mean(), npArr[[6,7,8]].mean()]
    meanCols = [npArr[[0,3,6]].mean(), npArr[[1,4,7]].mean(), npArr[[2,5,8]].mean()]

    #varRows = [np.var(npArr[0,1,2])]

    sumRows = [npArr[[0,1,2]].sum(), npArr[[3,4,5]].sum(), npArr[[6,7,8]].sum()]
    varRows = [np.var(sumRows), np.var(sumRows), np.var(sumRows)]
    stdRows = [np.std(sumRows, dtype=np.float64), np.std(sumRows, dtype=np.float64), np.std(sumRows, dtype=np.float64)]


    sumCols = [npArr[[0,3,6]].sum(), npArr[[1,4,7]].sum(), npArr[[2,5,8]].sum()]
    varCols = [np.var(sumCols), np.var(sumCols), np.var(sumCols)]
    stdCols = [np.std(sumCols, dtype=np.float64), np.std(sumCols, dtype=np.float64), np.std(sumCols, dtype=np.float64)]

    #3 by 3 Matrix 
    npArr3x3 = np.reshape(npArr, (3, 3))

    npmin = [np.amin(npArr3x3, axis=0).tolist(), np.amin(npArr3x3, axis=1).tolist(), min(list)]
    npmax = [np.amax(npArr3x3, axis=0).tolist(), np.amax(npArr3x3, axis=1).tolist(), max(list)]


    print(npmin)
    print(npmax)







    resDict = {
      'mean': [meanCols, meanRows, npArr.mean()],
      'variance':[varCols, varRows, np.var(npArr)],
      'standard deviation': [stdRows, stdCols, np.std(npArr)],
      'max': npmax,
      'min': npmin,
      'sum': [sumCols, sumRows, npArr.sum()]
    }

    return resDict




    # calculations = {}
    # ## min, max,
    # rowL = []
    # npColList = []
    # npRowList = []

    # for i in range(3):
    #   npColList.append(list[i:9:3])
    #   npRowList.append(list[i*3:i*3+3:1])

    # print(npColList) # columns
    # print(npRowList) # rows

    # #Method 1: use np.Array 

    # npArrayRows = np.array(npRowList)
    # npArrayColumns = np.array(npColList)

    # meanList = []

    # # first find max and min of each 


    # for j in range(3):
    #   meanList.append(np.mean(npArrayRows[j, :]))

    # print(meanList)


    
    # axis1sum = np.sum(npMatrix, axis = 0) 
    
    # axis2sum = np.sum(npMatrix, axis = 1) 
    
    # sumDict = [axis1sum, axis2sum, flattenSum]
    # calculations['sum'] = sumDict




    return calculations