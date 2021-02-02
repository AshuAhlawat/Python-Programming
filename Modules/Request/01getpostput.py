import requests

x=requests.get('https://myclass.lpu.in')
with open("myclass.html",'w') as f:
    f.write(x.text)
    
print(x.headers)

y= requests.get('https://d2skuhm0vrry40.cloudfront.net/2020/articles/2020-02-20-16-45/rust-makes-call-of-duty-modern-warfare-the-game-i-wanted-at-launch-1582217140107.jpg/EG11/resize/1200x-1/rust-makes-call-of-duty-modern-warfare-the-game-i-wanted-at-launch-1582217140107.jpg')

with open("Rustimagerequest.png",'wb') as f:
    f.write(y.content)
    
print("\n\n\n")

print(y.headers)
