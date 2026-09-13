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

