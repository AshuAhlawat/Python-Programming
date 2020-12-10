# libraries
import json

# main
x = '{"name":"Ashwani","age":30,"city":"New York"}'
print(x)
y = json.loads(x)
print(y)

# function
z = {"name": "Ashwani", "age": 19, "City": "Phagwara"}
m = json.dumps(z)
print(m)

person1 = {"name": "Ashwani Ahlawat", "age": 19, "city": "Bahadurgarh", "vehicle": "hero honda","sex": "undefined", "marital status": "single forever", "future occupation": "Job in NetFlix"}
p1_json=json.dumps(person1,indent=4,separators="\n""\t")
print(p1_json)