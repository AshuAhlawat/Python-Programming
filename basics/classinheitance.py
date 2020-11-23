# in this we can learn about class and how we can make a class with same attribute and method


class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        return self.fname.title() + " "+self.lname.title()


p1= person("ashwani","ahlawat")
p2 = person("gaurav", "patel")
p3 = person("ankit", "kumar")
p4 = person("swakshwar", "ghosh")

print(p1.printname())
print(p2.printname())
print(p3.printname())
print(p4.printname())


class alias_year(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def alias_method_year(self):
        return str(self.year)


p1 = alias_year("ashwani", "ahlawat", 2024)
print(p1.alias_method_year())

p2 = alias_year("gaurav", "patel", 2024)
print(p1.printname())
print(p2.alias_method_year())


class alias_age(alias_year):
    def __init__(self, fname, lname, year, age):
        super().__init__(fname, lname, year)
        self.age = age

    def alias_age_method(self):
        return self.printname()+" "+self.alias_method_year()+" "+str(self.age)


p1 = alias_age("ashwani", "ahlawat", 2024, 18)
p2 = alias_age("gaurav", "patel", 2024, 18)
print(p2.alias_age_method())
print(p1.alias_age_method())

