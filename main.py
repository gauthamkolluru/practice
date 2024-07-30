# age of a person as an input during the runtime... 
# and if the age is > 60 then print he/she is a senior citizen
# and if the age is > 30 < 60 then print he/she is a Working citizen
# else we want to print he he/she is a junior citizen

age = input("Enter age of a person: ") # "45"

age = int(age) # (integer) 45

if age > 60:
    print("Senior Citizen")
elif age > 30 and age < 60:
    print("Working Citizen")
else:
    print("Junior Citizen")
    
# Ternary If condition

# Single line if else statement

print("Senior Citizen") if age > 60 else print("Junior Citizen")

# idiomatic python / pythonic coding

