def SelectSort(s):
    tempLis = s
    res = []
    while len(tempLis) > 0:
        res.append(min(tempLis))
        tempLis.remove(min(tempLis))
    return res
