x = 5
def set_local_x(num):
    x = num
    print(x)

def set_global_x(num):
    global x
    x = num 
    print(x)

set_local_x(50)
print("this is global_x:",x)
set_global_x(55)
print("this below result is after change global x :")
print(x)