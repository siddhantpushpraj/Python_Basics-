'''
import math
pos=[0,0]
while True:
    s=input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else: pass

print(int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2))))
'''
'''
print (abs.__doc__)
print (int.__doc__)
print (raw_intput.__doc__)
def square(num):
'''
'''
    Return the square value of the 
    input number.
    The input number must be integer.
'''
'''
    return (num**2)
print (square(6) )
print (square.__doc__)
'''
'''
def s(x,y):
    return int(x)+int(y)
x=input()
y=input()
print(s(x,y))
'''
'''
x=int(input())
print(str(x))
'''
'''
def value(x,y):
    print(int(x)+int(y))
x=input()
y=input()
value(x,y)
'''
'''
def value(x,y):
    print(x+y)
x=input()
y=input()
value(x,y)
'''
'''
def check(a,b):
    if(len(a)>len(b)):
        print(a)
    elif (len(a) < len(b)):
        print(b)
    else:
        print(a)
        print(b)
a=input()
b=input()
check(a,b)
'''
'''
def even(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")
n=int(input())
even(n)
'''
'''
def printd(n):
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    print(d)
n=int(input())
printd(n)
'''
'''
def printd(n):
    d={}
    f=[]
    for i in range(1,n+1):
        d[i]=i*i
    for i in d.values():
        f=d.values()
    return f
f=[]
n=int(input())
f=printd(n)
print(f)
'''
'''
def printd(n):
    d={}
    f=[]
    for i in range(1,n+1):
        d[i]=i*i
    for i in d.values():
        print(i)
    #return f
f=[]
n=int(input())
printd(n)
#print(f)
'''
'''
def printd(n):
    d={}
    f=[]
    for i in range(1,n+1):
        d[i]=i*i
    for i in d.keys():
        print(i)
    #return f
f=[]
n=int(input())
printd(n)
#print(f)
'''
'''
def printd(n):
    d=list()
    for i in range(1,n+1):
        d.append(i**2)
    print(d)
n=int(input())
printd(n)

'''
'''
def printd(n):
    d=list()
    for i in range(1,n+1):
        d.append(i**2)
    print(d[:5])
n=int(input())
printd(n)
'''


