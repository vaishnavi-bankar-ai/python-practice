# using re.search() like find()
import re
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('From: ',line):
        print(line)
# using re.search() like startswith() to find a data from file:
print("re.search() like startswith() to extract a data from file:")
import re
hand = open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From: ',line):
        print(line)
# re.findall() : useful when we want the matching strings to be extracted.
import re
x='My 2 favourite numbers are 128 and 523 ONLY'
y= re.findall('[0-9]+',x)
print(y)
z=re.findall('[AEIOU]+',x)
print(z)
m=re.findall('[A-Z]+',x)
print(m)
x='My 2 favourite numbers are 128 and 523'
n=re.findall('[AEIOU]+',x)
print(n)
# Greedy Matching : to match the largest possible string:
import re
x='From: Using the :Character'
y=re.findall('^F.+:',x)
print(y)
