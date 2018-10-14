'''
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;
for x in lines:
    print (x)

'''
'''
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(values)
'''

'''
import math
c=50
h=30
value=[]
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
x=','.join(value)
print(x)
'''
'''
x=input("enter").split(',')
x.sort()
print(','.join(x))
'''
'''
x=input("enter").split(' ')
x.sort()
print(' '.join(x))
'''
'''
l=[]
l1=[]
s=0
x=(input())
l=x.split(',')
i=0
for j in l:
    c=int(j)
    i=0
    s=0
    while(c>0):
        s=int(s+(c%10)*pow(2,i))
        c=int(c/10)
        i=i+1

    if(s%5==0):
        l1.append(j)

print(','.join(l1))
'''
'''
l=[]
l1=[]
s=0


i=0
for j in range(1000,2100):
    c=int(j)
    i=0
    s=0
    p=0
    while(c>0):
        s=int(c%10)
        c=int(c/10)
        p=p+1
        if(int(s%2)==0):
            i=i+1

    if(i==p):
        l1.append(j)

print(l1)

'''
'''
l=0
w=0
s=input()
for c in s:
    if (c.isdigit()):
        l=l+1
    if (c.isalpha()):
            w = w+1
print("nuber ", l)
print("letter ", w)
'''
'''
l=0
w=0
s=input()
for c in s:
    if (c.isupper()):
        l=l+1
    if (c.islower()):
            w = w+1
print("upper ", l)
print("lower ", w)
'''
'''
a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)
'''
'''
x=input()
l=[]
for num in x:
    if((int(num)%2)!=0):
        l.append(num)
print(l)
'''


s=0
while True:



    print("d or D for deposite or W or w for withdrawal ")
    opt=str(input( " option"))
    if(opt=="D" or opt=="d" ):
        a = int(input("amount"))
        s=s+a
        
    elif (opt=="W" or opt=="w"):
        a = int(input("amount"))
        s=s-a
    else:
        break

print(s)








