        
list1=[1,1,2,2,2,3,3,3,4,4,5,5,6]

list2=[]

for i in list1:
    if(i not in list2):
        list2.append(i)
print(list2)    
        
    
##by function
def remove(list):
    list2=[]

    for i in list:
        if i not in list2:
            list2.append(i)
        
    return list2
list=[1,1,2,2,2,3,3,3,4,4,5,5,6]
print(remove(list))
