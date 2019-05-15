'''
Aim : Methods of list
'''
'''
Append Method
'''
l = list(map(int,input("enter values for list:").split( )))
a = l.append(5)
print(l)
'''
Extend Method
'''
l = list(map(int,input("enter values for list:").split( )))
n = list(map(int,input("Multiple Values for append in list").split( )))
lm = l.extend(n)
print(l)
'''
Clear Method:
'''
l = list(map(int,input("enter values of string").split()))
c = l.clear()
print(l)
'''
Copy Method
'''
l = list(map(int,input("enter values for list").split( )))
a = l.copy()
print(a)
'''
List is Mutable:
'''
l = [1,2,3,4,5,6,7,8]
l[2] = 23
print(l)
