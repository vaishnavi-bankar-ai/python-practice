fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    word = line.split()
    if len(word) >= 3:
        print(word[2])
#Double split pattern example code: to get  uct.ac.za from the data below
line= 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])



