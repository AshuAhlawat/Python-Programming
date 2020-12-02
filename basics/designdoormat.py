rows=int(input("Enter the number of height: "))
column=int(input("Enter the number of  breadth: "))
variable=rows//2+1
for i in range(1,variable):
    center=(i*2 -1)*".|."
    print(center.center(column,"-"))
print("WELCOME".center(column,"-"))
for i in reversed(range(1,variable)):
    center=(i*2-1)*".|."
    print(center.center(column,"-"))
    