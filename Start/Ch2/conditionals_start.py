# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 10000, 1000

# conditional flow uses if, elif, else
if x < y:
  print ("x is less then y")
elif x == y:
  print ("x equals y")
else:
  print ("x is greater then y")

# conditional statements let you use "a if C else b"
result = "x is less than y" if(x < y) else "x is greater or equal to y"
print(result)
