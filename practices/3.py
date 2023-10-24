from functools import cmp_to_key
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class stud: 
    def __init__(self, name, age, roll) -> None:
        self.age = age
        self.name = name
        self.roll = roll

    def compare(self, other):
        if self.roll == other.roll:
            if self.age == other.age:
                return self.name - other.name
            return self.age - other.age
        return self.roll - other.roll


a = [stud(input(), int(input()), int(input())) for i in range(10)]

# for stu in a:
#     print(stu.name, stu.age, stu.roll)

a.sort(key=cmp_to_key(stud.compare))

for stu in a:
    print(stu.name, stu.age, stu.roll)

print(a)