'''
#even odd
a=int(input("enetr a number"))
b=int(input("enetr a number"))

if(a%2==0):
    print("even")
    for i in range(a,b+1,2):
        print(i)
    print("odd")
    for i in range(a+1,b,2):
        print(i)    

for i in range(a,b+1):
    if(i%2==0):
        print(i,"even")
    else:
        print(i,"odd")
    
  
# table
a=int(input("enter a number"))
for i in range(1,11):
      print(a,"x",i," = ",a*i)
    
      

#pow

a=int(input("enter number"))
b=int(input("enter number"))
c=pow(a,b)
print(c)
'''
#fact
a=int(input("enter a number"))
m=1
for i in range(1,a+1):
    m=i*m
    
print(m)
'''
# sqr sum
a=int(input("enter number"))
b=int(input("enter number"))
c=pow(a,2)
d=pow(b,2)
e=c+d
print(e)

#leap year

for i in range(1900,2102):
    if(i%4==0):
        if(i%100!=0):
            print(i)

#series
a=int(input("enter range"))
c=1
for i in range(1,a+1):
    c=(pow(i,i)/i)+c
print(c)
'''
