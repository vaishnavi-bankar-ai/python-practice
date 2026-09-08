# def is a keyword stands for the definition of a function,define the function
# def is a keyword and it ends with :
def thing():
    print("Hello")
    print("Fun")
thing()
print("function's very basic code")
thing()
# max function: built-in function ; appearently lowercase letters are bigger than uppercase letters
# max function : basic practice code
big = max("Hello world")
print(big)
large = max("VirtualStudiocodecv")
print(large)
# min function: built-in function: appearently space is the smallest thing
# min function: basic practice code
tiny = min("Hello World")
print(tiny)
small = min("virtualStudioCodecc")
print(small)
#defining and calling/invoking the function :
# def keyword only defines the funcyion but does not automatically runs the code
# for execution part,we need to invoke/call the function that is function name()
# practice code for  defining and invoking function 
x=5
print("Hello")
def print_lyrics():
    print("I am okay")
    print("I work all day")
print("Yes")
print_lyrics()
x=x+2
print(x)
# parameter : parameter is a variable which we use in the function definition.
#practice code for parameter concept
def great(lang):
    if lang == 'es':
        print("Yes John")
    elif lang == 'fr':
        print("no John")
    else:
        print("Hello")
great("fr")
great('em')
great("es")


