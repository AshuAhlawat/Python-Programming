name=input("Enter your name here: ")

regd=str(input("Enter your registration number here: "))

if len(regd)==8:
    f=open("student details.txt","a")

    g=f.write(name+"\t"+regd[0:8]+"\n")

    f.close() 
else:
    print("Error! Registration Number must be of 8 digits")