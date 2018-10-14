'''
import sys
sys.version
sys.version_info
sys.api_version
sys.argv
'''
#sys.setrecursionlimit()
#
##text.wrap
'''
import textwrap
a=input()
b=textwrap.wrap(a,3)
m=[]
for i in b:
    c=textwrap.wrap(i,1)
    for j in c:
        if j not in m:
            m.append(j)
            #print(j)
    print("".join(m))
    m.clear()
'''

'''
x=input()
l=[]
l=x.split('@');
print(l[0])
'''
'''
x=input()
l=[]
l=x.split('@');
l1=l[1].split('.')
print(l1[0])
'''
'''
import re
s = input()
print (re.findall("\d+",s))

#method 2
s=input()
for i in s:
    if i.isdecimal():
        print(i)
'''

'''
unicodeString = u"hello world!"
print (unicodeString)
'''
'''
from decimal import *
n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))

print (round(sum,2))

'''
'''
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):

    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]


print(result)
'''
'''
from datetime import datetime, timedelta

N = 2

date_N_days_ago = datetime.now() - timedelta(days=N)

print (datetime.now())
print (date_N_days_ago)
'''
'''
col=int(input())
row=int(input())
mat=[]
mat1=[]
for i in range(col):
    for j in range(row):
        mat.append(i*j)
    mat1.append(mat)
    mat=[]
print(mat1)
'''