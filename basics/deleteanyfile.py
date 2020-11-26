import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("there is no file exist as this name")
