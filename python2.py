class Computer:
    def __init__(self):
        print("in init")

    def configi(self):
        print("i5, 8gb, 1tb")


com1 = Computer()
com2 = Computer()
com1.configi()
com2.configi()

print()


class Comp:
    def __init__(self, ram, cpu, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def configuration(self):
        print(self.cpu, self.ram, self.hdd)


com3 = Comp('i9','16GB','2TB')
com3.configuration()


class Com:
    def __init__(self):
        self.name = 'Rama'
        self.age = 21

    def update(self):
        self.age = 21

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Com()
c2 = Com()
c2.name = "Seetha"
c2.age = 20
c2.update()

print(id(c1))
print()
print(c1.name)
print()
print(c2.age)
print()
print(c2.name)
print()
if c1.compare(c2):
    print("Rama gets a job")
else:
    print("RAMAGETS A JOB")

print()

class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.company = 'BMW'


car1 = Car()
car1.mil = 8
print(car1.mil, car1.company)
print()
print(car1.wheels)


class Student:

    school = 'GKHS'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class.. in abc molude")

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
         self.m1 = value


s1 = Student(34,47,32)
s2 = Student(89,32,12)

print(s1.set_m1(89))

print(s1.avg())
print(Student.getSchool())
print(s1.get_m1())
print(s1.m1)
Student.info()


class Stud:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "Acer"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.ram, self.cpu)


si = Stud('Rahiman', 68)
sii = Stud('Chaitanya', 69)


sii.show()
si.show()


class A:
    def feature_1(self):
        print('hai')
    def feature_2(self):
        print('Hai There!!')


class B():#class B(A) in some cases, then remove #comment for super().__init__() in B
    def __init__(self):
        #super().__init__()
        print("in B init")
    def feature_3(self):
        print("hello")
    def feature_4(self):
        print("Hello There!!")


a1 = A()
a1.feature_1()
a2 = B()
a2.feature_3()
#a2.feature_2()


class C(A, B):

    def __init__(self):
        super().__init__()#if B is not subclass of A and c wants to be subclass for both a and b. then multiple inheitance works

    def feature_5(self):

        print("GM")

    def feature_6(self):
        print("Gm spectalur")


a3 = C()
a3.feature_1()#class A's feature
a3.feature_3()#class B's feature
a3.feature_6()#own class feature


class PyCharm():
    def execute(self):
        print("Best IDE")
        print("Easy Debugging")
        print("line -by line execution Environment not supports")

class Laptops():
    def code(self, ide):
        ide.execute()

ide = PyCharm()
lap1 = Laptops()
lap1.code(ide)

a = 5
b = 6
print(a+b)
e = '5'
d = 'World'
print(int.__add__(a,b))

print(str.__add__(e, d))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s30 = Student(m1, m2)

        return s30

s9 = Student(45, 48)
s10 = Student(49, 50)
s30 = s9 + s10
print(s30.m1)
