a=int(input())
width=len("{0:b}".format(a))
for i in range(0,a+1):
    print("{0:{width}d}" "{0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))