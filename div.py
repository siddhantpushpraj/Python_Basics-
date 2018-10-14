'''
#divisible by 5 and 7
i=500
while(i>=500 and i<=2700):
    if(i%7==0 and i%5==0):
        print(i,end=" ")
    i=i+1

#divisible by 3 and 5
i=1

while(i>=1 and i<=50):
    
    if(i%7==0 ):
        print("buzz",i)
    if(i%3==0 ):
        print("fizz",i)
    if(i%3==0 and i%5==0):
        print("fizz buzz",i)     
    
    i=i+1

#rev
i=int(input("enter a number"))

while(i>=0):
    print(i)
    i=i-1
            
'''
#series
n=6
s=0.0
for i in range(1,n):
    print(i,"/",i+1,"+"," ",end=" ")
print("n/n+1",end=" ")
for i in range(1,n+1):
    a=float(i/(i+1))
    s=s+a
print("=",s )   
    
