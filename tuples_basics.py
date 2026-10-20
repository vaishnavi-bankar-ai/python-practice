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
