#File IO SYSTEM
#"r"for reading
#"w"for writing
#"a"for append
#"r+"/"w+" for read and write
#"x" for creating any file
#---------------------------------------------------------------------------
f=open("demofile.txt","w")
g=f.write("\nSwakshwar Ghosh Ign DIngo")
print(g)
f.close()

