#Logical operators
#and,or,not

print(True and False)#F
print(False and True)#F
print(True and True)#F

a=int(True)
print(a)#1
a=int(False)
print(a)


print(1 and 0)#0
print(18 and 0)#0
print(0 and 'string')#0
print('abc' and 'abc2')#abc2
print(11 and 22)# 22
print('' and 'abc')# ' '

print('abc' or 'abc2')#abc
print('' or 'abc')# abc

print(not False)#True
print(not True)# False







#equality operators
#==,!=
a=10
b=20
print(a==b)#F
print(a!=b)#T


x=10
y=10
print(x==y)#T


"""
x
 ------------------10
y
"""

x1=[1,2,3]
y1=[1,2,3]

#x1----------------[1,2,3]

#y1---------------[1,2,3]

print(x1==y1)# T

x1=[1,2,3]
y1=[1,2,3,4]

#x1----------------[1,2,3]

#y1---------------[1,2,3,4]

print(x1==y1)#F

z1=10.0
z2=10
print(z1==z2)




#Assignment operators
#=,+=,-=,*=,/=
#i++,i--

a=10
a+=1# a=a+1
print(a)#11
a=a+2# 13
a=a+1# 14
a+=3 #17
print(a)

x=4
x-=1 # x=x-1
print(x)#3
x=x-2
print(x)#1

#Special operators
#Identity Operators
#is,is not
a=10
b=20
print(id(a))
print(id(b))
print(a is b)# F

a=10.0
b=10
print(id(a))
print(id(b))
print(a is b)# F
print(a==b)#T

#/,//
#==,is

a=[1,2,3,4]
y=[1,2,3,4]
print(a==y)# T
print(a is y)# F




#Membership operators
#in,not in
l=[1,2,3,4,5,7,10,30]
print(1 in l)#T
print(10 in l)#F
print(100 not in l)#T

s="python"
print('z' in s)#F
print('p' not in s)#F
print('n' in s)# T
print('yth' in s)# T

