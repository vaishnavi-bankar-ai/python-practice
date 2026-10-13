print([1,99.9,'red'])
print(['red','yellow'])
print(['well',[2,'red',65],86.5])
print([[10,20],[30,40,50]])
print([])
#find any single element in a string:
friends=['Neha','Katha','Eva']
print(friends[1])
print(friends[2])
print(friends[0])
# len() function: to find a length of a list
print("length of a list:",len(friends))
#range() function: thr range function returns a list of numbers that range from zero to one less than the parameter.
print(list(range(9)))
print(list(range(len(friends))))
for i in range(len(friends)):
    friend=friends[i]
    print("Happy New Year:",friend)
