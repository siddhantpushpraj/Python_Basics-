'''
class base:
    def __init__(self):
        self.name="john"
    def display(self):
        print(self.name)
class derived(base): #class derived(base): -->error
    def disp(self):
        print("hi")
obj=derived()
obj.display()
obj.disp()

'''
'''
class base:
    def __init__(self):
        self.name="john"
    def display(self):
        print(self.name)
class derived(base): #class derived(base): -->error
    def disp(self):
        print("hi1")
class derived2(derived): #class derived(base): -->error
    def disp2(self):
        print("hi2")
obj=derived2()
obj.display()
obj.disp()
obj.disp2()
'''

###multilevel
'''
class base:
    def __init__(self):
        self.name="john"
    def display(self):
        print(self.name)
class base2:
    def disp(self):
        print("hi1")
class derived2(base,base2):
    def disp2(self):
        print("hi2")
obj=derived2()
obj.display()
obj.disp()
obj.disp2()
'''

#method overloading
'''
class base:
    def __init__(self):
        self.name="john"
    def display(self):
        print(self.name,"base")
    def show(self):
        print("hi base")
class derived(base): #class derived(base): -->error
    def __init__(self):
        self.name="hello"
    def display(self):
        print(self.name)
    def show(self):
        print("derived")
obj=derived()
obj.display()
obj.show()
'''
#wap that have derived two class rect and triangle and find area
'''
class polygon:

    def __init__(self,a,b):
        self.a=a
        self.b =b

class triangle(polygon):
    def disp(self):
        print("triangle ",self.a*self.b/2)
class rectangle(polygon):
    def disp2(self):
        print(" rectangle ",self.a*self.b)
a=int(input())
b=int(input())
obj=triangle(a,b)
#obj.display()
obj.disp()
obj2=rectangle(a,b)
obj2.disp2()
'''
#wap that as a class person inherit a class faculty from person which also has class publication
#wap to find bill.the user have option to pay by cheque or cash.use inheritance.


## method overloading
'''
class human:
    def sayhello(self,name=None):
        if name is not None:
            print("hello"+name)
        else:
            print("hello")
obj=human()
obj.sayhello()
obj.sayhello("john")

'''
'''
def add (datatype,*args):
    if datatype=='int':
        ans=0
    if datatype=="str":
        ans=" "
    for i in args:
        ans=ans+1
        print(ans)
add("int",5,6)
add("str","hello ","john")
'''