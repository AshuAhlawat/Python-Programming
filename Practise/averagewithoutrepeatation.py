def average(array):
    set_inp=set(array)
    list_inp=list(set_inp)
    a=0
    for ele in list_inp:
        a+=ele
    return a/len(list_inp)

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)