(x,y,z)=(4,'jan',22.8)
print(x,y,z)
d=dict()
d['csev']=2
d['cwen']=4
for (k,v) in d.items():
    print(k,v)
tups=d.items()
print(tups)
#tuples are comaprable:
print((0,1,2)<(5,1,0))
print((0,1,20000)<(0,3,4))
print(('Jones','Sally')<('Jones','Sam'))
print(('jones','Sally')>('Adams','Sam'))
print(('AbC','def')>('abc','DEF'))
#sorting of tuples
#sort by key:
d={'a':10,'c':22,'b':1}
print(d.items())
print(sorted(d.items()))
d={'w':10,'s':22,'u':1}
t=sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)
#sort by value:
m={'a':10,'c':22,'b':1}
tmp=list()
for k,v in m.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp, reverse=True)
print(tmp)
#exercise: find 10 most common words in a file using tuples:
name=input("Enter a file name: ")
fhand=open(name)
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts) # printed counts dictionary
lst=list()
for (k,v) in counts.items():
    newtup=(v,k)
    lst.append(newtup)
lst= sorted(lst,reverse=True)
print(lst)
for v,k in lst[:10]:
    print(k,v)
 