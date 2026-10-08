#String Concatenation
a="hello"
b = a + "there"
print(b)
c = a + " " + "there"
print(c)
#Use of in as a logical operator
fruit = input("fruit name:")
print('n' in fruit)
print("m" in fruit)
print("nan" in fruit)
print("bal" in fruit)
if "a" in fruit:
    print("Found it !")
#string comparison :
word = input("enter a word:")
if word == "banana":
    print("All right, bananas.")
if word < "banana":
    print("Your word," + word + ", comes before banana.")
elif word > "banana":
    print("Your word," + word + ", comes after banana.")
else:
    print("All right,bananas")
