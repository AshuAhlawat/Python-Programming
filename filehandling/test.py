
f=open("student details.txt","r")
g=f.readlines()
for line in g:
    while  True:
        try:
            required_number = str(input("Enter regd no: ")) 
            if required_number in line:
                print(line)
                break;
            else:
                print("4O4 not found")
            continue