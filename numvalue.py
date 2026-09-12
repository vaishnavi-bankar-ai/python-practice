largest_so_far=-1
print("before",largest_so_far)
for the_num in (9,41,12,3,74,15):
    if the_num > largest_so_far:
        largest_so_far= the_num
    print(largest_so_far, the_num)
print("after" ,largest_so_far)
#find smallest value :example code
smallest_so_far = -1
print("before",smallest_so_far)
for the_num in (9,41,12,3,74,15):
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far,the_num)
print("after",smallest_so_far)

