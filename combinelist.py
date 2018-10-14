'''
l1=['hi','bye']
l2=['shy','why']
l3=[]
n1=(len(l1))
n2=(len(l2))

for i in range(n1):
    for j in range(n2):
        x=l1[i]+l2[j]
        l3.append(x)
        
print(l3)        

###
l1=['she','he','why','hi']

l3=[]
n1=(len(l1))


for i in l1:
    l3.append(i[0])
        
print(l3)     

'''
###

list2=[]
list1=[1,2,3]
def function(list1):
    
   for i in range(len(list1)):
            
           b=list1[i]*10
           list2.append(b)
function(list1)
print(list2)

