# print("Hail python!") for 3 times

# `for` loop

# collection of values... a single variable pointing to multiple values... 

# range()

# range(3) -> 0 - 2 (n-1 = 3-1)

# print("program with for loop")

# for val in range(3):
#     print("Hail python! ", val)

# Range() 

# things that we pass to a function are called as ARGUMENTS
# things that are accepted by the function as called as PARAMETERS

# Range(start, stop, step)

# start -> from where the count must start...... the default value is 0
# step -> tell what number to add to each value of the function ... the default is 1

# => 0+1, 1+1, 2 (0,1,2..n-1)

# stop parameter defines at what value the range function must stop its execution. 

# range(5).... 4 (n-1, n = 5)


# case 1: 0 - 10 step = 1: output = 0,1,2,3,4,5,6,7,8,9

# for i in range(0, 10, 1):
#     print(i, end=', ')

# case 2: 0 - 11 step = 1: output = 0,1,2,3,4,5,6,7,8,9,10

# for i in range(0, 11, 1):
#     print(i, end=', ')

# case 3: 1 - 11 step = 1: output = 1,2,3,4,5,6,7,8,9,10

# for i in range(1, 11):
#     print(i, end=', ')

# case 4: 0 - 11 step = 2: output = 0, 2, 4, 6, 8, 10

# for i in range(0, 11, 2):
#     print(i, end=', ')

# case 5: 0 - 11 step = 3: output = 0, 3, 6, 9

for i in range(0, 11, 3):
    print(i, end=', ')