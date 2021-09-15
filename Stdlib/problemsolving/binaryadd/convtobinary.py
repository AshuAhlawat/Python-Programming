def dec2bin(num):
    binary=[]
    rev_binary=[]
    while num>1:
        rev_binary.append(int(num%2))
        num /= 2
    for i in range(len(rev_binary)-1,-1,-1):
        binary.append(rev_binary[i])
    if (allsame(binary)):
        binary.insert(0,1)

    x = ''
    for i in range(len(binary)):
        j = str(binary[i])
        x+=j
    x= int(x)
    return x
    

def allsame(binary):    
    first= binary[0]
    for i in range(len(binary)):
        if first != binary[i]:
            return False
    return True