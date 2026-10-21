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
#Search and replace: replace() function is like a 'search and replace' operation in a word processor
#it replaces all occurrences of the search string with the replacement string
rain = line.replace('Bob' , 'Jane')
print(rain)
rin= line.replace("o","x")
print(rin)
#stripping whitespace: lstrip() , rstrip(), strip() functions : removes whitespace at the left, right and at the both end respectively
print(line.lstrip())
print(line.rstrip())
print(line.strip())
# to find a prefix of a string: startswith() function
word = "please have a nice day"
print(word.startswith("please"))
print(word.startswith("P"))
# parsing and extracting ; to extract only a part of an entire string
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
