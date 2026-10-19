counts=dict()
print('Enter a line of text: ')
line=input('')
words = line.split()
print('Words: ',words)
print('Counting: ')
for word in words:
    counts[word] = counts.get(word,0)+1
print('counts',counts)
#defintie loops and dictionaries: for loop goes through all of the keys in the dictionary and looks up the values
counts={'chuk':1,'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])
