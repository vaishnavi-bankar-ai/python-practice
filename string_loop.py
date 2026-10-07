#to find each characters in a string using while loop
fruit=input("fruit name:")
index=0
while index < len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
