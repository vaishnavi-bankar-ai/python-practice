import re
name=input('Enter a file name: ')
hand=open(name)
total=0
count=0
for line in hand:
    line=line.rstrip()
    num=re.findall('[0-9]+',line)
    for n in num:
        total=total+ int(n)
        count=count+1
print("There are",count,"values with a sum =",total)
hand.close()
