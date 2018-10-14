'''
def fact(x):
    if x == 0:
        return 1

    return x * fact(x - 1)
x=int(input())
print(fact(x))
'''
'''
n=int(input("enter number"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)
'''
'''
l=[]
values=input()
for i in values:
    l.append(i)

t=tuple(l)
print (l)
print (t)
###or
values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)
'''
