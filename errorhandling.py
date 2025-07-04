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
