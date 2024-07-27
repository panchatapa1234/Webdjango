class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showName(self):
        print("Name =", self.name)
    def showAge(self):
        print("Age =", self.age)
class Student(Person):
    def __init__(self, n, a, r):
        super().__init__(n, a)
        self.rollno = r

    def showRollno(self):
        print("Roll Number =",self.rollno)

s1= Student("Panchatapa",21,118)
s1.showName()
s1.showAge()
s1.showRollno()

