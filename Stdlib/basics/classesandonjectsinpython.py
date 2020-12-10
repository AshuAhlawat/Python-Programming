class person:
    def __init__(self, name, section):
        self.name = name
        self.section = section

    def myfunc(self):
        print("My name is "+self.name+" and my section is "+self.section)


p1 = person("Ashu", "KOCQB")
p2 = person("Gaurav", "KOCQB")
p3 = person("Anky", "KOCQB")
p4 = person("Swaksh", "KOCQB")
print(p1.name, p1.section)
print(p2.name, p2.section)
print(p3.name, p3.section)
print(p4.name, p4.section)
p1.myfunc()
p2.myfunc()
p3.myfunc()
p4.myfunc()
p1.section = "KOCQB-G1"
p1.myfunc()


class teacher:
    pass
