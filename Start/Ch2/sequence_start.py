# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
print(len(mylist))

# to access a member of a sequence type, use []
# print(mylist[2])
# print(mylist[-1])
# mylist[0] = 10
# print (mylist[0])

# # add a list to another list
# # another_list = [1,5,9]
# # mylist = mylist + another_list
# # print(mylist)

# # mystr = "This is a string"
# # print(mystr[2])

# # use slices to get parts of a sequence
# print(mylist[::2])

# # you can use slices to reverse a sequence
# # print(mylist[::-1])

# # Tuples are like lists, but they are immutable
# mytuple = (0,1,2, "three")
# # print(mytuple[1]) #The vaules of indexes can't be changed
# #Therefore it has better memory

# # Sets are also sequences, but they contain unique values
# myset = {1,2,3,4,2,"hey"}
# print(myset)# They force uniquness in their members 
# # Set, however, can not be indexed like lists or tuples
# # print(myset[0]) # this will cause an error

# # Test for membership
# print (1 in mylist)
# print (3 in mytuple)
# print (5 in myset)
