'''
num=int(input())
den=int(input())
try:
    div=num/den
except:
    print("cannot divide by 0")

'''
'''
try:
    num=input()
    d=num/0
except KeyboardInterrupt:
    print("KeyboardInterrupy")
except ValueError:
    print("ValueError")
except:
    #print(int(num)**2)
    print("bye")
finally:
    print("successfully")
'''
'''
def Divide(num,deno):
    return(num/deno)
try:
    Divide(10,0)
except:
    print("error")
else:
    print("prog trminate")

'''
'''
try:
    f=open("C:\\Users\\Dell\\Desktop\\python3\\file.txt","x")
    f=open("C:\\Users\\Dell\\Desktop\\python3\\file.txt","rt")

except IOError:
    print("file already or does't exit1")
finally:
    f = open("C:\\Users\\Dell\\Desktop\\python3\\file.txt", "rt")
'''
n = int(input())
for i in range(n):
    try:

        a = int(input()).split(" ")
        print(int(a[0]) / int(a[1]))


    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: $")
