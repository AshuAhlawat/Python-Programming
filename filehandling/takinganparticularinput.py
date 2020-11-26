import re
required_number=str(input("Enter the regd no you want: "))


f=open("student details.txt","r")
g=f.readlines()
for line in g:
    if required_number in line:
        print(line)
        break
else:
    print("4O4 not found")

