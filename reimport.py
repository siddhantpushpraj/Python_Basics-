import re
###
'''
if re.search('hi(pe)*','hidedede'):
    print("match found")
else:
    print("not found")
'''
###
'''
pattern='she'
string='she sells sea shells on the sea shore'
if re.match(pattern,string):
    print("match found")
else:
    print("not found")

'''
###
'''
pattern='sea'
string='she sells sea shells on the sea shore'
if re.match(pattern,string):
    print("match found")
else:
    print("not found")

'''
###
'''
pattern=r'[a-z A-Z]+ \d+'
string='Lx 12013,Xyzabc 2016,i am indian'
m=re.findall(pattern,string)
for n in m:
    print(n)

'''
###
'''
pattern=r'[a-z A-Z]+ \d+'
string='Lx 12013,Xyzabc 2016,i am indian'
m=re.finditer(pattern,string)
for n in m:
    print('match at start index',n.start())
    print('match at start index', n.end())
    print(n.span())
'''

'''
pattern=r'[a-z A-Z]+ \d+'
string='Lx 12013'
m=re.findall(pattern,string)
for n in m:
    print(n)
'''
# Q.A program that uses a regular expression to match string which starts with a
#    sequence of digit follwed by blank or space, arbitary character.
'''
import re
a='LXI 2013,XYZ abc 2016,I am an Indian $%5^'
pattern='[a-zA-Z]+[!@#$%&()_] +'
m=re.findall(pattern,a)
for n in m:
    print(n)
'''
# Q.WAP to extract charcter from a string using a regular expression.
'''
import re
a=input()
pattern='[a-zA-Z]+ '
m=re.findall(pattern,a)
for i in m:
    print(i)
'''
# Q.A program  to print first word of string.
'''
import re
a=input()
pattern='[a-zA-Z]+ '
m=re.findall(pattern,a)
for i in m:
    print(m[0])
    break
    '''
# Q.program to print char in pairs
'''

import re

a = input()
pattern = '[a-zA-Z]+'
m = re.findall(pattern, a)
x=m.split("2")
for i in x:
    print(i)

'''
# Q.print only first two character of every word.
'''
import re
a=input()
pattern='[a-zA-Z]+'
m=re.findall(pattern,a)
for i in m:
    print(i[0:2])
'''
##Q wap to check if string contains only alphabet and digits only
'''

a=input()
pat='[a-zA-Z]'
if re.search(pat,a):
    if re.search('[0-9]',a):
        print(a)
'''
##QUE to match if string contains 1 a followed by 0 or more b's ie ab* .a,ab,abbbb...


##QUE text="the qiuck brown fox jumps over the lazy dog".search for the following pattern.pattern fox dog horse.
##(b)to find location of fox in a given text
'''
s="the quick brown fox jump over the lazy dog horse"
p1='fox'
p2='dog'
p3='horse'
m=re.findall(p1,s)
n=re.findall(p2,s)
b=re.findall(p3,s)
if(m):
    if(b):
        if(n):
            print("VALID : ",s)
        else:
            print("INVALID")
    else:
         print("INVALID")
else:
     print("INVALID")
'''
'''

s="the quick brown fox jump over the lazy dog horse"
p1='fox'
m=re.search(p1,s)
s=m.span()
print("index",s)zzzz
'''
#Que pularize the word list=[bush,fox,toy,cat]
'''
li=['bush','fox','toy','cat','half','knife']
for x in li:
    if(x[len(x)-1]=='f'):
        print(x[0:len(x)-1]+'ves')
    elif (x[len(x) - 2] == 'f'):
        print(x[0:len(x) - 2] + 'ves')
    elif (x[len(x) - 1] == 'x' or x[len(x) - 1] == 'h'):
        print(x+'es')
    else:
        print(x + 's')

def pluralize(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'
list1=['bush','fox','toy','cat','half','knife']
for i in list1:
    pluralize(i)
    print(x)

'''
##Que a website req  user to input password and user name,write a programm to validate the password.
##at least one letter from a-z,A-z,@#$,length=6-12
'''
value = []
x=input()
items=x.split(',')
for p in items:
    if ((len(p)>6 or len(p)<12)):
        if (re.findall("[a-z]",p)):
            if (re.findall("[0-9]",p)):
                if (re.findall("[A-Z]",p)):
                    if (re.findall("[$#@]",p)):
                        value.append(p)
print (",".join(value))

'''
