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
