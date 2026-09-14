count = 0
print("before", count)
for thing in [3,41,12,9,74,15]:
    count= count + 1
    print(count,thing)
print("after", count)
# summing/totaling in a loop 
sum=0
print("before",sum)
for thing in[9,41,12,3,74,15]:
    sum= sum+thing
    print(sum,thing)
print("after",sum)
#Finding average in a loop
count = 0
sum = 0
print("before","count:", count,"sum:", sum)
for value in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+value
    print(count,sum,value)
print("after","count:",count,"sum:",sum,"Average:",sum/count)
#filtering in a loop
print("before")
for value in [9,41,12,3,74,15]:
    if value>25:
        print("large number:",value)
print("after")
#search using a Boolean variable
found=False
print("before",found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found= True
    print(found,value)
print("after",found)
#loop assignment code for max and minimum value
largest=None
smallest=None
while True:
    num = input("enter a number:")
    if num == "done":
        break
    try:
        n=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = n
    elif n> largest:
        largest= n
    if smallest is None:
        smallest=n
    elif n < smallest:
        smallest=n
print("Maximum is",largest)
print("Minimum is",smallest)
print("loop topic concepts are clear")
