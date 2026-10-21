def greet(name):
    if name == "jn":
        return "John"
    elif name == "mi":
        return "Michael"
    else :
        return "hey stranger"
print(greet("mr"), "who are you?")
print(greet("mi"), "how are you?")
print(greet("jn"), "where are you")
#functions: multiple parameters/arguments topic code
def addtwo(a,b):
    print(a)
    return a+b
    print(b) # when python reaches return,the function ends immediately and hence print(b) will never execute in this function
x = addtwo(10,20)
print(x)
