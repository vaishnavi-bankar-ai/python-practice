name =  input("Enter a file name: ")
fhand= open(name)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word]= counts.get(word,0)+1
print('words: ',words)
print('counts: ',counts)
# to find out which words comes maximum times in a file and also their count
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count> bigcount:
        bigword=word
        bigcount=count
print('word_max: ',bigword,'and count is : ',bigcount)
