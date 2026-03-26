class teacher:
    def __init__(self,fname,lname,qualification,tdomain):
        self.fname=fname
        self.lname=lname
        self.qualification=qualification
        self.tdomain=tdomain
    
    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

teacher1=teacher("anuj","Kaushal","Mtech at iit delhi","Python")
teacher2=teacher("mayank","kumar","Mtech at iit bombay","Physics")

print(teacher1.fname)
print(teacher.fullname(teacher1))
print(teacher2.fullname())