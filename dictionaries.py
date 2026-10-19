cabinet=dict()
cabinet['Summer']=12
cabinet['fall']=3
cabinet['spring']=75
print(cabinet)
print(cabinet['fall'])
cabinet['fall']=cabinet['fall']+25
print(cabinet)
ooo={}
print(ooo)
# get() method use in dictionaries for counting 
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name]= counts.get(name,0)+1
print(counts)