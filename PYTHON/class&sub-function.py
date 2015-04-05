'''
Created on 2015/4/5

@author: fmir33
'''
class Student:  
    def __init__(self, name, grade, age):  
        self.name = name  
        self.grade = grade  
        self.age = age  
    def set_name(self, name):  
        self.name = name  

student_objects=[]
student_objects.append( Student('john', 'B', 15) )
student_objects.append( Student('dave', 'A', 12) )
student_objects.append( Student('jane', 'A', 10) )
student_objects[0].set_name('John')

for i in student_objects:
    print i.name,i.grade,i.age