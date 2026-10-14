fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    word = line.split()
    if len(word) >= 3:
        print(word[2])

