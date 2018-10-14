'''
import re
value = []
items=[x for x in input().split(',')]

for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
'''
'''
# example code:
string_with_newlines = """something
someotherthing"""

import re

print (re.match('some', string_with_newlines)) # matches
print (re.match('someother',string_with_newlines)) # won't match
print (re.match('^someother', string_with_newlines,re.MULTILINE)) # also won't match
print (re.search('someother',string_with_newlines)) # finds something
print (re.search('^someother', string_with_newlines,re.MULTILINE)) # also finds something

m = re.compile('thing$', re.MULTILINE)

print (m.match(string_with_newlines)) # no match
print (m.match(string_with_newlines, pos=4)) # matches
print (m.search(string_with_newlines,re.MULTILINE)) # also matches
'''
'''
import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)>6 or len(p)>12:
        if(re.search("[a-z]",p)):
            if (re.search("[A-Z]", p)):
                if (re.search("[0-9]", p)):
                    if (re.search("[@#$]", p)):
                        value.append(p)

print(value)
'''
'''
# initialize
a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["Nick",  30, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])
# sort the table by age
import operator
a.sort(key=operator.itemgetter(0,1,2))

# print the table
print (a)
'''
'''
from operator import itemgetter, attrgetter
l = []
while True:
    s=input()
    if  not s:
        break
    l.append(tuple(s.split(",")))
print (sorted(l, key=itemgetter(0,1,2)))
'''
n=0
freq={}
x=input().split()
for word in x:
    freq[word]=n+1

words=(freq.keys())
##l=words.sort()
for w in words:
    print(w,freq[w])
