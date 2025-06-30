#this section shown examples about primitive datatypes 
"""
primitive datatypes is about the arthmetic expression 
like addition
subtraction division and modules"""
#first seen about simple arthmetic problem....
a = 10

b = 20

print(a+b)#this is simple math
print(a-b)
print(a*b)
print(a/b)
print(a%b)

"""the above code is showed primitive datattypes in python"""


'''order execution is main rules in computer programming 

there is called as bodmas rules...

b->bracket
o->power
d->division
m->multiplication
a->additon
s->substraction '''
print("im from bodmass rules")
a=2
b=3
print((a+b**2+(a+b)**2)/2)


#datatypes of python not for python only all programming lang using same syntax of datatypes
'''
integer
float
string
boolean

these are the datatypes in python'''


#examples of integer 

a= 10 #this whole number thier is no floating values :
print("this is integer value :{}".format(a))

a= 10.0 #this whole number thier is no floating values :
print("this is float value :{}".format(a))

a= "dheena" #this whole number thier is no floating values :
print("this is string value :{}".format(a))

a= 1 #this whole number thier is no floating values :
print("this is Bool positive value :{}".format(bool(a)))

a= 0 #this whole number thier is no floating values :
print("this is Bool negative value :{}".format(bool(a)))



'''next we recap for comparision opertor in pythonss....
there are six types in comparision operator in python..such that
== ->
!= ->
> ->
< ->
>= ->
<= ->
these types are basically used in true or false in python so that is called as comparision '''

#using if else to see examples of comparison operators....

a= 30

b = 40

if(a==b):
    print("a is equal to b ")
else:
    print("a is not equal to b")

if(a!=b):
    print("yes a is not equal to b")
else:
    print("no a is equal to b")

if(a>b):
    print("yes a is greater than b")
else:
    print("no a is not greater than b")

if(a<b):
    print("yes a is less than b")
else:
    print("no a is less than b")

if(a>=b):
    print("yes a is grater than equal")
else:
    print("no its not greater than equal of a and b...")
if(a<=b):
    print("yes this less is  than a b")
else:
    print("no this is not a less than b ..")


#next one is chaining comparision 

''' this chaining comparision used like gates comparision examples 
And Gates
Or gates 
Not gates '''

'''first see examples of and gates 

a b r 
0 0 0
0 1 0
1 0 0
1 1 1
these is rules of and gates 
'''

#this is example of and gate using symbol of & 

if(10<100 & 100>10): #1+1=1
    print(True)
else:
    print(False)

if(10<100 & 100<10): #1+0=0
    print(True)
else:
    print(False)

if(10>100 & 100>10):#0+1=0 
    print(True)
else:
    print(False)

if(10<100 & 100<10): #0+0=0
    print(True)
else:
    print(False)