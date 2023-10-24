import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from functools import cmp_to_key

class member:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age

    def intro(self):
        return f"Hi, My name is {self.fname} {self.lname}. I am {self.age} year old."
    
    def cmp(self, other):
        if self.age == other.age:
            return (self.fname + self.lname) >= (other.fname + other.lname)
        return self.age - other.age
    

class teacher(member):
    def __init__(self, fname, lname, age, salary)->None:
        super().__init__(fname, lname, age)
        self.salary = salary

    def intro(self):
        return super().intro() + f"\nMy Salary is {self.salary}"
    
    def cmpsalary(self, other):
        if self.salary == other.salary:
            return super().cmp(other)
        return self.salary - other.salary

class student(member):
    def __init__(self, fname, lname, age, roll) -> None:
        super().__init__(fname, lname, age)
        self.roll = roll
    def intro(self):
        return super().intro() + f"\nMy rollno is {self.roll}"
    
    def cmproll(self, other):
        if self.roll == other.roll:
            return super().cmp(other)
        return self.roll - other.roll

t = []
for i in range(5):
    fn, ln, age, sal = [x for x in input().split()]
    t.append(teacher(fn, ln, int(age), int(sal)))

t.sort(key=cmp_to_key(teacher.cmpsalary))

for i in t:
    print(i.intro())

stu = []
for i in range(5):
    fn, ln, age, roll = [x for x in input().split()]
    stu.append(student(fn, ln, int(age), int(roll)))

stu.sort(key=cmp_to_key(student.cmproll))

for i in stu:
    print(i.intro())