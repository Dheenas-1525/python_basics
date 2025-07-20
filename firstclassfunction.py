def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_40 = create_adder(10)
print((add_40(100)))

def greet(name):
    return f"Hello, {name}!"

def call_function(func, value):
    return func(value)

print(call_function(greet, "Dheena"))
# ➜ Hello, Dheena!


x = 5
y = 4
print(lambda x: x>3, x)
# print(map(x,y))
print(lambda y: y>3, y)

print(lambda dheena: x>2, x)