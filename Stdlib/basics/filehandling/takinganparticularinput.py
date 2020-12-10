f=open("student details.txt","r")
lines=list(f.readlines())
print(lines)
switch=0
while switch == 0:
    regno=str(input("Registeration No : "))
    for line in lines:
        if regno in line:
            print(line)
            switch=1
            break
        else:
            switch=0
    if switch==0:
        print("404 Not Found")
f.close()


