class stud():
    def __init__(self,name,registration,section,course,institution):
        self.name=name
        self.regd=registration
        self.sec=section
        self.crs=course
        self.inst=institution
    
    def __str__(self):
        return '[' + self.name +','+str(self.regd)+']'
    def call(self):
        print('My name is ',self.name,' having registration number ',self.regd,' is in section ',self.sec,' is enrolled is the course ',self.crs,' in ',self.inst)
    def correct_regd(self,registration):
        self.regd=registration

x=stud('ashu',12016043,'KOCQB','Btech-CSE(DATA SCIENCE)','LPU,Phagwara,Punjab')
y=stud('Gaurav','12014982','KOCQB','Btech-CSE(DATA SCIENCE)','LPU,Phagwara')
x.correct_regd(12018777)
x.call()
y.call()
