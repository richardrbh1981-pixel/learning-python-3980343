#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
from os import path
import time
from datetime import datetime

# Print the name of the OS
# print(os.name)

# Check for item existence and type
# print("Item exists: ", path.exists("textfile.text.bak"))
# print("Item is a file: ", path.isfile("textfile.text.bak"))
# print("Item is a directory: ", path.isdir("textfile.text.bak"))

# # Work with file paths
# print("Item's path: ", path.realpath("textfile.text.bak"))
# print("Item's path and name: ", path.split(path.realpath("textfile.text.bak")))

# # Get the modification time
# t = time.ctime(path.getmtime("textfile.text.bak"))
# print(t)
# print(datetime.fromtimestamp(path.getmtime("textfile.text.bak")))

# Calculate how long ago the item was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime("newfile.text"))
print("File has been modified %.2f hours ago" % (td.total_seconds()/3600)) # 2f is 2 decimal places

