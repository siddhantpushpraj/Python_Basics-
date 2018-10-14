'''
l=[]
for i in range(2000,3201):
    if((i%7==0) and (i%5!=0)):
        l.append(i);
print(l)
'''
'''
a=int(input('Enter number'))
f=1
while(a>0):
    f=f*a
    a=a-1
    print(f,end=',')

'''
'''
n=int(input('Enter element'))
d=dict()
for i in range(1,n+1):
    d[i]=i*i 
 
print(d)
'''

'''
values=int(input('Enter element'))
l=values.split(",")
t=tuple(l)
print(l)
print(t)
'''



