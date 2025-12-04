# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function

print("my integer is ",myint)
print("my string is ",mystr)
# Operators are used to perform operations on variables
# print("my int added to my flot",myint + myfloat)
# print("my int times my flot",myint * myfloat)
# print("my int divided by my flot",myint / myfloat)
# another_str = "this is another string"
# print("string added", mystr + another_str)
# print("nom " * 3)
# Logical and comparison operators 
# print(myint == 10)
# print(myfloat != 20)
# print(myint > 20)
# print(myfloat < 10)
# print(myint > 5 and myfloat <25.0)
# print(not(myint > 5 and myfloat <25.0))
# re-declaring a variable works
myint = "abc"
print("change int to string", myint)