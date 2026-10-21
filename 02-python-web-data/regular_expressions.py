# using re.search() like find()
import re
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('From: ',line):
        print(line)
# using re.search() like startswith() to extract a data from file:
print("re.search() like startswith() to extract a data from file:")
import re
hand = open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From: ',line):
        print(line)
