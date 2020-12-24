#8-1

def create_student(name, korean, math, english, science) :
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

students = [
    create_student("1",1,1,1,1),
    create_student("2",2,2,2,2),
    create_student("3",3,3,3,3),
    create_student("4",4,4,4,4)
]

# print("이름","총점","평균",sep="\t")

import numpy as average

# 한번에 print 하기.. 별로 안이쁘네...
for student in students :
    print(student["name"],
        sum([student[i] for i in student if type(student[i]) == int]),
        average.array([student[i] for i in student if type(student[i]) == int]).mean()
    )

#여기서 __init__ 은 한개밖에 안됨.
class Student :

    def __init__(self,name,korean,math,english,science) :
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def sum(self) :
        return self.korean + self.math + self.english + self.science

    def average(self) :
        return average.array([self.korean,self.math,self.english,self.science]).mean()


student1 = [
    Student("1",1,1,1,1),
    Student("3",3,3,3,3),
    Student("5",5,5,5,5),
    Student("7",7,7,7,7)
]

for student in student1 :
    print(student.name, student.sum(), student.average())


    # print(student.name,
    #     sum([i for i in student if type(i) == int]),
    #     average.array([i for i in student if type(i) == int]).mean()
    # )




    #8-2
    
    #인스턴스가 어떤 클래스로 만들어졌는지 확인가능 파이썬은.


class Student2 :
    def __init__(self) :
        pass

student2 = Student2()
print(isinstance(student2,Student2))

print(isinstance(student1[0],Student))

# 단순한 인스턴스 확인

print(type(student2)==Student2())


# 만약에 클래스의 변수가 접근한정자가 private 으로 하고 싶으면 앞에다 __ 두개만 넣으면 된다.

# getter-setter 
# private 한 radius 를 간접적으로 접근.
# 여기서 안전하게 사용하려면 먼가 setter 할때의 value 에 대한 조건문을 걸고 그 조건문에 해당되지 않으면 raise 해서 오류 발생시키면된다.


def get_radius(self):
    return self.__radius
def set_radius(self, value):
    self.__radius = value


#상속

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("__init__ 호출")
    def test(self):
        print("test()")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child init")

child = Child()
child.test()
print(child.value)