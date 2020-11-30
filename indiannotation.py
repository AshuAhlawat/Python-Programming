notaion = int(input("Enter the currency here: "))
input_list = list(str(notaion))
input_len = len(input_list)
res = ""
if input_len <= 3:
    print(notaion)
elif input_len >= 4:
    for i in range(-3, -input_len-1, -3):
        input_list.insert(i, ",")
for i in input_list:
    res += i
print(res)