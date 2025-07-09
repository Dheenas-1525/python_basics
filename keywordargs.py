def add(x, *y):
    print(x)
    print(y)

    r = 0
    r = r + x
    # print(r)
    for i in y:
        r = r + i
    return r
print("addition result : {}".format(add(1,2,3,4,5,6,7,8,9)))




def letters(x, *y):
    print(x)
    print(y)

    r = 0
    r = r + x
    # print(r)
    for i in y:
        r = r + i
    return r
a,b,c,d,e,f,g,h = 1,2,3,4,5,6,7,8
print("letters Given : {}".format(letters(a,b,c,d,e,f,g,h)))



def letters(x, *y):
    print("First letter:", x)
    print("Remaining letters:", y)
    result = x
    for letter in y:
        result += letter
    return result

# Example with letters
print("Letters Given: {}".format(letters("a", "b", "c", "d", "e", "f", "g", "h")))



def keywords_args(e, l, a, **kwargs):
    print(kwargs)
    return kwargs
# keywords_args = (1, 2, 3, h=1, b=2, c=3, d=4)
keywords_args(1, 2, 3, h=1, b=2, c=3, d=4)
