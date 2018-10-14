import re
### QUE
'''
wap which repeatdly read number until user enter done.once done is enter print our the the total term

if the user enter anything other than number detect an error skip to another number.
'''
'''
try:
    sum=0
    i=0
    while(True):
        num = input()
        if(num=='done'):
            break
        elif(num.isdigit()):
            sum=sum+int(num)
            i=i+1
    print(sum/i)
except:
    print("invalid")

'''
'''
try:
    sum=0
    i=0
    while(True):z
        num = input()
        if(num=='done'):
            break
        elif(num.isdigit()):
            sum=sum+int(num)
            i=i+1
        else:
            print("invalid1")
    print(sum/i)
except ValueError:
    print("invalid")
'''

# A program using reject to remove leading zero from IP address
'''
l=[]
ip=input()
string=re.sub('\.[0]*','.',ip)
print(string)

'''
##QUE A python program to extract year month and date from a string
import re
x=input()
result=re.findall('\d{2}-\d{2}-\d{4}',x)
print(result)
