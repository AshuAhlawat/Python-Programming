import os
if os.path.exists("demofile.txt"):
    os.remove("student details.txt")
else:
    print("there is no file exist as this name")
