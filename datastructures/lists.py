list = [1,  4.6, 'python', False] 
#       0     1        2            3    <----- these are the index values

list[1] = 5.5

print(list)

my_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# splitting takes integar value which starts from 0

split_function = my_list[0:7]

print(split_function)

# my_list list contains 7 elements which means 0-6 index so above 6 the index value wont take so the programme wont run. 

#python accepts negative values also if any one type below my_list[-1] it will print saturday as saturday is the last element of the list

print_index = my_list[6]

print(print_index)


#Membership operators 'in' or 'not in'


my_list1=[1,2,3,4,5,6,9,7,8]

bool_return=0 not in my_list1

print(bool_return)

bool_return1=22 in my_list1

print(bool_return1)