# def add(a,b):
#     return a+b

# a = 10
# b = 20
# print(add(a,b)) this is simple add fucntion 

#basic calculator:
# def calculator(add, sub, multi, div, mod):
#     return add(a+b)
#     return sub(a-b)
#     return multi(a*b)
#     return div(a/b)
#     return mod(a%b)

# value = input("enter the values of a:")
# value2 = input ("enter the values of b:")
# print(add(value,value2))
# print(sub(value,value2))
# print(multi(value,value2))
# print(div(value,value2))
# print(mod(value,value2))

def calculator(a,b):
    print("add",a+b)
    print("sub",a-b)
    print("multi",a*b)
    if b!=0:
        print("div",a/b)
        print("mod",a%b)
    else:
        print("cant divide by zero pls check it values")
        
value1 = int(input("enter the value of a:"))
value2 = int(input("enter the value of b:"))

calculator(value1,value2)