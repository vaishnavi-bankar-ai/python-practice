n=7
while n>2:
    print(n)
    n=n-1
print("Blastoff!")
print("n=",n)
#Zero trip loop:loop never executed because its never enter in a loop
# zero trip loop : example code
n=0
while n>0:
    print("hello")
    print("Fun")
print("Ohh Sorry")
#break statement/breaking out of loop : It ends the current loop and jumps to the statement immediately following the loop
#in simple words,break statement means escape or quit the loop immediately and go to next statement of a code
while True:
    line = input(">")
    if line == "done":
        break
    print(line)
print("Done!")
#continue statement:finishing an iteration with continue: it ends the current iteration and jumps to the top of the loop ans starts the next iteration
print("New version")
while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("it's Done!")
