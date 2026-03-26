class Students:
    no_of_students=2
    raise_marks=5
    def __init__(self,fname,lname,marks):
        self.fname=fname
        self.lname=lname
        self.marks=marks
        Students.no_of_students+=1

    def apply_raise(self):
        self.marks=int(self.marks + self.raise_marks)
        pass

std1=Students("anuj","Kaushal",90)
std2=Students("mayank","kumar",93)

std1.raise_marks=1.03
print(std1.__dict__)
print(std2.__dict__)


print(Students.raise_marks)
print(std1.raise_marks)

print(std2.apply_raise())

print(std2.marks)
print(std1.marks)