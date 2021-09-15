def comparetriplet(a, b):
    ares = 0
    bres = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            ares += 1
        if b[i] > a[i]:
            bres += 1
    
    return([ares, bres])

comparetriplet([1,2,4], [4,2,1])