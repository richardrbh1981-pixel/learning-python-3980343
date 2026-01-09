# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
sample_file = open("textfile.text", "w+")
sample_file.write("Cool these are the secret documnets\n" +
"So don't just put them in any codespace\n" )
sample_file.close()

# Open the file for appending text to the end
sample_file = open("textfile.text", "a+")

# write some lines of data to the file
sample_file.write("If this line is here someone has alterd the file.\n")
sample_file.write("Welp it happens I guess.\n")

# close the file when done
sample_file.close()