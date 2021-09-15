#the array is of size 5

def minmaxsum(arr):
    sum1 = (arr[1]+arr[2]+arr[3]+arr[4])
    sum2 = arr[0]+arr[2]+arr[3]+arr[4]
    sum3 = arr[0]+arr[1]+arr[3]+arr[4]
    sum4 = arr[0]+arr[1]+arr[2]+arr[4]
    sum5 = arr[0]+arr[1]+arr[2]+arr[3]
    res = [sum1,sum2,sum3,sum4,sum5]
    print(min(res),max(res))

minmaxsum([7, 69, 2, 221, 8974])
    
    