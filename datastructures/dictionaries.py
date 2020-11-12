ages = {"Ashwani": 18, "Gaurav": 18, "Swakshwar": 20}

print(ages["Swakshwar"])

print("Sarthak" in ages)

print(ages.get("Sarthak"))

n = ages.get("Sarthak")

print(n is None)

######################################################################################
# compound dictionary

student_about = {'Ashwani Ahlawat': {'Subject': 'B-Tech Cse', 'Section': 'KOCQB', 'Group': 'A'},'Swakshwar ghosh': {'Subject': 'B-Tech Cse', 'Section': 'KOCQB', 'Group': 'A'}}
print(student_about)
print(student_about['Ashwani Ahlawat']['Subject'])