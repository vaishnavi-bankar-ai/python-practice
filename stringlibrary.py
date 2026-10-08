#string library: python has number of string functions which are in a string library
#these functions are already built into every string - we invoke them by appending the function to the string variable
# these functions do not modify the original string, instead they return a new string that has been altered
# lower case and upper case fubctions in a string library
line = input ("Enter a string:")
zap = line.lower()
print(zap)
nap = line.upper()
print(nap)
#find() function to search for a substring
# if substring is not found, find() returns -1
fin = line.find("na")
print(fin)
fam = line.find('z')
print(fam)
