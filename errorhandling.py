a = 10
b = [1,2,3,4]
c = 2

try:
    c = a + b[c]
    print(c)
except NameError as e:
    print("name error happened")
    print(e)
except IndexError as e:
    print("index error happended")
    print(e)

else:
    print("all good")

finally:
    print("whatever the case is i will work")

""" this above code os basic template of python error handling"""



#class_error_handling_code



def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("cant divide by zero")
        return a/b
try:
    c = divide(5, 0)
    print("value of c is {}".format(c))
except (NameError, IndexError, KeyError) as e:
    print("NameError happened : {}".format(e))
except ZeroDivisionError as e:
    print("ZeroDivisionError: {}".format(e))
else:
    print("all good working code")

finally:
    print("subam......")

l = [1,2,3,4,5,6,7,8,9]
l = iter(l)

print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
