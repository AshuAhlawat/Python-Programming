#given_list=[100,100,80,45,45]
#x=int(input("Enter the number here: "))
#given_list.append(x)
#given_list.sort()
#given_list.reverse()
#for i in given_list:
#    for n in range(1,len(given_list)):
#        print(i)
#--------------------------------------------------------------------
num_of_students=int(input("Enter the Number of the students: "))
num=[]
for i in range(1,num_of_students+1):
    number=int(input("Enter the marks of {} student: ".format(i)))
    num.append(number)
num.sort(reverse=True)
str_num_of_quantity=str(num_of_students)
for i in num:
    for n in range(1,int(num_of_students)):
        
        print(i)