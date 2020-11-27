f=open("student details.txt","r")
g=f.readlines()
f.close()
print(g)
index_to_remove=int(input("Enter index number: "))
del g[index_to_remove]
f_n=open("student details.txt","w+")
for n in g:
    f_n.write(str(n))

f_n.close()
