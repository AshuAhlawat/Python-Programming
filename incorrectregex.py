import re
x=int(input())
for i in range(x):
    case=input()
    ans=True
    try:
        y=re.compile(case)
    except re.error:
        ans=False
    print(ans)
