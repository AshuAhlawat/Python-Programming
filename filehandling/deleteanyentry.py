f=open("student details.txt","r+")
g=f.readlines()
for line in g:
    if line.strip("\n")!="Gaurav Patel 12015555":
        line.pop()
        break
f.close()
