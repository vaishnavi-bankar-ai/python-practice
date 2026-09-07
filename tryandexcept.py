astr = "Hello Bob"
try:
    istr=int(astr)
except:
    istr=-1
print("First", istr)
astr="123"
try:
    istr=int(astr)
except:
    istr=-1
print("Second",istr)

#try and except structure practice
astr="Bob"
try:
    print("hello")
    istr=int(astr)
    print("there")
except:
    istr=-1
print("Done",istr)
# add input function into the try and except structure code :
rawstr= input("Enter a number:")
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print("Nice Work")
else:
    print("Not a Number")    
    