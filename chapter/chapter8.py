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