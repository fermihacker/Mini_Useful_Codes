def bubbleSort(array):
    tempLis = array
    for i in range(len(tempLis) - 1):
        for j in range(len(tempLis) - 1):
            if tempLis[j] > tempLis [j+1]:
                tempLis[j], tempLis[j+1] = tempLis[j+1], tempLis[j]
    return tempLis
