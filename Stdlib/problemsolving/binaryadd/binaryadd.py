from convtobinary import dec2bin
from bin2dec import bin2dec

def binadd(num1,num2):
    dec1 = bin2dec(num1)
    dec2 = bin2dec(num2)
    dec_res = dec1+dec2
    dec2bin(dec_res)
    

binadd(11,10)