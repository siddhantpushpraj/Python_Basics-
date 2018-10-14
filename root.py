a=float(input("enter coff of x^2 " ))
b=float(input("enter coff of x "))
c=float(input("enter value of c "))
i=pow(b,2)
f=4*a*c
d=i-f
if(i<f):
    print("imaginary root")
else:
    x=(-b-(d**0.5))/(2*a)
    print(x)
    x=(-b+(d**0.5))/(2*a)
    print(x)
              
