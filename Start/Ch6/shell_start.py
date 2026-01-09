#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
from datetime import datetime
import os
from os import path
import shutil
from zipfile import ZipFile


# make a duplicate of an existing file
if path.exists("newfile.text"):
    
    # get the path to the file in the current directory
    src = path.realpath("newfile.text")
        
    # # let's make a backup copy by appending "bak" to the name
    # backup = src + ".bak"

    # # now use the shell to make a copy of the file
    # shutil.copy2(src, backup)

    # # rename the original file
    # os.rename("testfile.text", "newfile.text")

    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", 'zip', root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", 'w') as newzip:
        newzip.write("newfile.text")
        newzip.write("testfile.text.bak")

