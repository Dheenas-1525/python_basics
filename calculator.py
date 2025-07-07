#this code is im thinking to develop calculator app using python 
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if(b != 0):
        return a/b
    else:
        print("cant divide by zero")


def mod(a,b):
    if(b != 0):
        return a%b
    else:
        print("cant mod by zero")

calculator_app = {
    "1":add,
    "2":sub,
    "3":multi,
    "4":div,
    "5":mod
}

a = int(input("enter first number to calculate : "))

b = int(input("enter second number of to calculate  :  "))


print("==================================================")
print("The Choice OF This Calculator App :")

print("1):Addition")
print("2):sub")
print("3):multi")
print("4):div")
print("5):mod")


# print("Enter The Choice What You Want TO Calculate :  ")

choice = input("Enter the Choice Which One You Want ...! : ")

if choice in calculator_app:
    result = calculator_app[choice](a,b)
    print("Result is  :",result)
else:
    print("Something Wrong check .....?")