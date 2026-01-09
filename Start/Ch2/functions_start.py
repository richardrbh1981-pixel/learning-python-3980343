# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# hello_func()

# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you doing?")
# hello_func("What's up?")



# function that returns a value
# def cube(x):
#   return x * x * x

# result = cube(100)
# print(result)


# function with default value for an parameter

# def hello_func(greeting, name = None):
#   print("hello world!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting, name)

# hello_func("Nice to meet you", "Joe")

# function with variable number of parameters
def multi_add(start, *args):
  result = start
  result = 0
  for x in args:
    result = result + x
  return result

print(multi_add(100,50,600,800))