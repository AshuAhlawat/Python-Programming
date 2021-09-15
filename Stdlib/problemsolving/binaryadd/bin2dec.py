def bin2dec(num):
    ini_array = []
    for i in str(num):
        ini_array.append(int(i))
    
    j = 0
    dec_num = 0
    for bin in range(len(ini_array)-1,-1,-1):
        elem = ini_array[bin] *(2**j)
        dec_num += elem
        j+=1
    return dec_num