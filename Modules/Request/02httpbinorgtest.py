import requests

payload={'page':2,'count':25}

r=requests.get('https://httpbin.org/get',params=payload)
print(r.text)

print(r.url) #creates the needed url for us with the given parameters in the json file

payload1={'username':'dingo','password':1234}
p=requests.post('https://httpbin.org/post',data=payload1)
p_dict=p.json()
print("\n\n\n")
print(p_dict['form'])

print("\n\n\n")

o=requests.get('http://httpbin.org/basic-auth/dingo/1234',auth=('dingo','1234'))
print(o.text)
print(o.json())
print(o)

#delibarertly given wrong info wrt the url to get the not authorized response
m=requests.get('http://httpbin.org/basic-auth/dingo/1234',auth=('ashu','1234'))
print(m)
