'''
class xyz:
    var=10
obj1=xyz()
print(obj1.var)
'''
'''
class xyz:
    var=10
    def display(self):
        print("hi")
obj1=xyz()
print(obj1.var)
obj1.display()
'''
##constructor
'''
class xyz:
    var=10
    def __init__(self,val):
        print("hi")
        self.val=val
        print(val)
        print(self.val)
obj1=xyz(10)
print(obj1.var)
'''
'''
class xyz:
    class_var=0
    def __init__(self,val):
        xyz.class_var+=1
        self.val=val
        print(val)
        print("class_var+=1",xyz.class_var)
obj1=xyz(10)
obj1=xyz(20)
obj1=xyz("sid")
print(obj1.val)
'''

##wap with class employee keeps the track of number of employee in a organisation and also store thier name, desiganation and salary
'''
class comp:
    count=0
    def __init__(self,name,desigantion,salary):
        comp.count+=1
        self.name=name
        self.desigantion=desigantion
        self.salary=salary
        print("name ",name,"desigantion ",desigantion,"salary ",salary)
obj1=comp("sid","ceo","150000")
obj12=comp("rahul","manager1","150000")
obj3=comp("danish","manger2","150000")

'''
#wap that has a class circle use a class value define the vlaue of the pi use class value and calculate area nad circumferance
'''

class circle:
    pi=3.14
    def __init__(self,radius):
        self.area=self.pi*radius**2
        self.circum=self.pi*radius*2
        print("circumferance",self.circum)
        print("area", self.area)

radius=int(input())
obj1=circle(radius)

'''
#wap that have a class person storing dob of the person .the program subtract the dob from today date to find whether the person is elgoble for vote or vote
'''
import datetime
class vote:
    def __intit__(self,name,dob):
        self.name=name
        self.dob=dob
    def agevote():
        today=datetime.date.today()
        print(today)

obj1=vote("siddhant",1997)
obj.agevote()

'''
# ACCESS SPECIFIED IN PYTHON
## 1) .__ (private variable) 2)._ (protected variable)
'''
class abc:
    def __init__(self,var,var1):
        self.var=var
        self.__var1=var1
    def display(self):
        print(self.var)
        print(self.__var1)
k=abc(10,20)
k.display()
print(k.var)
# print(k.__var1) #private
print(k.__abc__var1)

'''
##wap uses classes to store the name and class of a student ,use a list to store the marks of three student
class student:
    mark=[]

    def __init__(self,name):
        self.name=name
        self.mark=[]
    def getmarks(self,sub):
        for i in range(sub):
            m=int(input())
            self.mark.append(m)
    def display(self):
        print(self.name,"  ",self.mark)
print("total student")
n=int(int(input()))
print("total subject")
sub=int(input())

s=[]
for i in range(n):
   print("student name")
   name=input()
   s=student(name)
   s.getmarks(sub)
   s.display()
