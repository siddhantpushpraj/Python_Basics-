'''
def printd(n):
    d=list()
    for i in range(1,n+1):
        d.append(i**2)
    print(d[-5:])
n=int(input())
printd(n)
'''
'''
def printd(n):
    d=list()
    for i in range(1,n+1):
        d.append(i**2)
    print(d[5:])
n=int(input())
printd(n)
'''
'''
def printd(n):
    d=[]
    for i in range(1,n+1):
        d.append(i**2)
    print(d)
n=int(input())
printd(n)
'''
'''
def printd(n):
    d=[]
    for i in range(1,n+1):
        d.append(i)
    print(d[:int(n/2)])
    print(d[int(n/2):])
n=int(input())
printd(n)
'''
'''
def printd(n):
    d=[]
    d2=[]
    for i in range(1,n+1):
        d.append(i)
    for i in d:
        if(i%2==0):
            d2.append(i)
    return d2
d2=[]
n=int(input())
d2=printd(n)
print(d2)
'''
'''
item=[]
while True:
    s=(input())
    if s:
        item.append(s)
    else:
        break


item.sort()
print(" ".join(item[-2:-1]))
print(",".join(item))
'''

'''
class American(object):
    pass
class NewYorker(American):
    pass
anAmerican = American()
aNewYorker = NewYorker()
print (anAmerican)
print (aNewYorker)
'''