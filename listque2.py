import random

a=[]
l1=[]
l2=[]
i=0
m=0
n=int(input("Enter number of elements:"))

for j in range(n):
       a.append(random.randint(1,100))

print('Randomised list is: ',a)
for j in range(n):
    if(a[j]%2==0):
        l1.insert(i,a[j])
        i=i+1
    else:
        l2.insert(m,a[j])
        m=m+1
print("even list",l1)
print("odd list",l2)
