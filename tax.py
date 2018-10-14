income=int(input("enter sal"))
if(income<=150000):
    print("no tax")
if(income>=150001 and income<=300000):
    i=float(income*10)/100  
    print("tax = ",i)
if(income>=300001 and income<=500000):
    i=float(income*20)/100  
    print("tax = ",i)
if(income>=500001 ):
    i=float(income*30)/100  
    print("tax = ",i)   
    
