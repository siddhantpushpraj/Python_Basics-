'''
#sum
i=1
c=0
while(i<11):
    c=i+c
    i=i+1
    
print("sum ",c)    

# number
i=1
while(i<11):
    c=i+c
    print(i,end=" ")
    i=i+1
    
   
#astrike
i=1
while(i<21):
    
    print("*",end=" ")
    i=i+1

# -1 to exit
c=0
d=0
i=int(input("enter"))
while(i!=-1):
    if(i>0):
        c=c+1
    if(i<0):
        d=d+1
    i=int(input("enetr number"))
print("postive number",c)
print("negetive number",d)               

#sum of digits
num=int(input("enter"))
c=0
while(num!=0):
    d=num%10
    c=d+c
    num=int(num/10)
print(c)

#reverse
num=int(input("enter"))
c=0
while(num!=0):
    d=num%10
    c=d+c*10
    num=int(num/10)
print(c)

#GCD
a=int(input("enter"))
b=int(input("enter"))
i=1
x=1
if(a<b):
    while(i<=b):
        if((a%i)==0):
            if((b%i)==0):
                x=i
        i=i+1        
if(a>b):

    while(i<=a):
        if(b%i==0):
            if(a%i==0):
                x=i
        i=i+1         
print(x)                
'''


        
