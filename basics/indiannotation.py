#constrains= len of the input is must not be greater than 10 digits
notaion = int(input("Enter the currency here: "))
input_list = list(str(notaion))
input_len = len(input_list)
res = ""
input_list.reverse()
for i in range(3, (input_len-3)*2, 3):
    input_list.insert(i, ",")
input_list.reverse()
for i in input_list:
    res += i
print(res)