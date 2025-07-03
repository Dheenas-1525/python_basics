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

#this is example of or gates :
'''rules of or gates
a b r 
0 0 0
0 1 1
1 0 1
1 1 0 '''



print("helloe this is from OR gates.....")

if(10<100 or 100>10):#1+1=0
    print(False)
else:
    print(True)


if(10>100 or 100>10):#0+1=1
    print(True)
else:
    print(False)

if(10<100 or 100>10):#1+0=1
    print(True)
else:
    print(False)

if(10<100 or 100<10):#0+0=0
    print(False)
else:
    print(True)

#datatypes memory management:
a=1
b=1
print(id(a))
print(id(b))

a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(id(a))
print(id(b))

#mutuable and imutable datatype:
string = ['hello world']
print(string)

for i in range (len(string[0])):
    print("letters in {} -> {}".format(string[0][i],i))

print(string[0][6])

# string[0][6]='u'

# print(string)#this will  not work becuase string is immutable 

#message idication
d="dheena"
msg=("brue wyane is {d}".format(d=d))
print(msg)


#string concordintion:
a = 'dheena'

b= 'dhayalan'

c= a + ' ' + b # if need space use this open bracket wiht space ...

print(c)


#collections of python :
''' there are four types of collection in python 
1)list
2)tuple
3)dictionaries
4)set

these are the collections  in python '''

#first to see list in python 

#syntax of list :
list =[]
#this is syntax of list

list=['dheena', 'dhayalan', 'subraja', 'sridhar']
print(list)
print(len(list))

list[3]='dheena'

print(list)#this one is work so list mutubale 

list.append('karthi')

print(list)


list.remove('dheena')

print(list)

list.pop(2)

print(list)


l=[1,2,3,4,5,6,7,8,9]
print(l)

print(l[1:5])

print(list[1:3])

new_list = list[::1]

print(new_list)

print(new_list[::-1])

# num = list(range(0, 101))
# print(num)

#in keyword:

name = 'dheena'

print(name)

if 'dheena' in name:
    print(True)
else:
    print(False)


#tuple syntax:
t=tuple()
'''this is the syntax empty tuple'''
t=('dheena', 'dhayalan')
print(t)
print(type(t))

print(t[0])

# t[0]='subraja'
# print(t)


#packing and unpacking:
a=0
b=0
c=0

t=(1,2,3)

a,b,c=t

print(a,b,c)



c=0
d=0
f=0

tupe=(1,2,3,4,5)

c,d,*f=tupe
print(c,d,f)


#dictionaries

#creating empty dictionaries:
d={}
d=dict()

print(type(d))
print(type(d))

dic = {"one":1,"two":2,"three":3}
print(dic)

del dic['one']

print(dic)


#sets

es=set()

es={1,2,3,4,5}

print(es)

print(type(es))


es={1,1,2,3,3,4,4,5,6}
print(es)

# sets={"name":dheena,"name":karthi,"name":dheena}
# print(sets)

my_dict = {
    "name": "dheena",
    "name": "karthi",
    "name": "subraja"
}
print(my_dict)  # {'name': 'subraja'} — only the last one kept
print(type(my_dict))

es_1 = {"dheena",'dhayalan','dheena','dhayalan'}
print(es_1)
print(type(es_1))


lis=[]
print(type(lis))

tu=()

print(type(tu))


lis = ['dheena', 'akni', 'raj']
print(lis)

lis[1] = 'dheena'

print(lis)

tup = ('dhena', 'akni', 'raj')
print(tup)

# tup[1]='dheena'
# print(tup)# so tuple is imuttable

'''control structure or control flow and iterable :
use this control flow if ellif and else '''

var = 5
if(var > 10):
    print("yes var greater then ten")
elif(var<10):
    print("yes var is lesser than ten")
else:
    print("no nothing is greater and lesser then ten ..")



var = 50
if(var > 10):
    print("yes var greater then ten")
elif(var<10):
    print("yes var is lesser than ten")
else:
    print("no nothing is greater and lesser then ten ..")

#loops:
'''there are two types of loops in every programming'''
#for loop

my_name='dheena'

for i in range(len(my_name)):
    print("letter in my name : {} -> {}".format(i,my_name[i]))
print("total letters of my_name is -> {}".format(len(my_name)))