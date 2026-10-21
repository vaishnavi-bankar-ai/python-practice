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
#concatenating(adding) two existing lists to create a new list:
a=[1,'dolly',20.5]
b=[30,58,'John']
c= a+b
print(c)
# list can be sliced using slicing operator:
t=[9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
# sorting of a list: 
print(friends)
friends.sort()
print("sorted list is:",friends)
#building a new list using a append method:
stuff=list()
stuff.append('book')
stuff.append(23)
print(stuff)
stuff.append('cookie')
print(stuff)
stuff.append([100,200,'moon'])
print(stuff)
friends.append(['Abhi','Rushi'])
print(friends)
for i in range(len(friends)):
    friend=friends[i]
    print("Happy New Year:",friend)
# other built in function to perform basic mathematical operations on a list:
print("length:",len(t))
print("max:",max(t))
print("min:",min(t))
print("sum:",sum(t))
print("average:", sum(t)/len(t))
#to find average of a list:
numlist=list()
while True:
    inp= input("enter a number:")
    if inp == 'done':
        break
    value=float(inp)
    numlist.append(value)
    average = sum(numlist)/len(numlist)
print("Average of a list:",average)

