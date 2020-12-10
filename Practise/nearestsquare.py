num = int(input("Enter your num here: "))

i = 1
result = 1

while result < num:
    i += 1
    result = i**2

lesser_than_result_square_number = (i-1)**2
higher_than_square_number = result
if higher_than_square_number - num <= num - lesser_than_result_square_number:
    print(higher_than_square_number)
else:
    print(lesser_than_result_square_number)
