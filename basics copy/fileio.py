#File IO SYSTEM
#"r"for reading
#"w"for writing
#"a"for append
#"r+"/"w+" for read and write
#"x" for creating any file
#=============================================================================>>
name=input("Enter your name:")
regd=input("Enter your regd no.:")

f=open("student details.txt","a")
g=f.write(name+"\t"+regd+"\n")
print(g)
f.close()

h=open("student details.txt","r")
j=h.read()
print(j)