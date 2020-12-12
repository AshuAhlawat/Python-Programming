import numpy

operations=['trunc','fix','floor','ceil']

for i in operations:
    print(eval('numpy.{}([-3.1666, 3.6667])'.format(i)))

print(numpy.around(3.16667,2))