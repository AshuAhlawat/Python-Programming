f = open("student details.txt", "r")

lines = f.readlines()
f.close()

new = open("student details.txt", "w")
for line in lines:
    if line.strip("\n") != str(input("Enter the name and regd number: ")):

        new.write(line)

new.close()