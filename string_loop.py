#to find each characters in a string using while loop
fruit=input("fruit name:")
index=0
while index < len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
#to find each character in a string using for loop(definite loop)
fruit=input("new fruit name:")
for letter in fruit:
    print(letter)
#to identify how many times a certain character comes in a string(find a count of a particular character in a string):
word=input("enter a name:")
count=0
for letter in word:
    if letter == "a":
        count= count+1
print(count)
#to find/get only a piece/part of a string:
p=input("enter a whole string:")
print(p[0:4])
print(p[6:7])
print(p[6:20])
print(p[:7])
print(p[9:])
print(p[:])
