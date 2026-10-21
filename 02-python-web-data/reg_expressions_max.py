import re
name=input("Enter a file name: ")
hand=open(name)
lst=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]*)',line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    lst.append(num)
print("Maximum: ", max(lst))
