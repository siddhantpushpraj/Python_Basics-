'''
##
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d1.update(d2)
d1.update(d3)
print(d1)
##
sum=0
list2=[]
list1=[10,20,30,40]
for i in range(0,len(list1)):
    sum=sum+list1[i]
    list2.append(sum)
print(list2)

##
d1={}
if(len(d1)==0):
    print("empty")


##
list1={'1':10,'2':20,'3':30,'4':40}
print(sum(list1.values()))

##
key=['0','1','2']
values=['sum','mon','tues']
x=dict(zip(key,values))
print(x)
'''
##
x=input("enter ")
l=[]
c=0
for i in range(0,len(x)):
    if(len(x[i]%2==0)):
        print(x[i])

