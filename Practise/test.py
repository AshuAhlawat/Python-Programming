import os
import math
import re
import sys
def simpleArraySum(ar):
    thesum=0
    for i in ar:
        thesum+=i
    return thesum




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()