#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("newfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("newfile.txt")
        
    # # let's make a backup copy by appending "bak" to the name
    # dst = src + ".bak"

    # # now use the shell to make a copy of the file
    # shutil.copy() copies over the file's content,
    # but does not copy over the original file's metadata,
    # such as the creation and modification times and other properties
    # shutil.copy(src, dst)

    # # rename the original file
    # os.rename("textfile.txt", "newfile.txt")
    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    # with keyword lets you create a local scope
    # that simplifies working with objects
    with ZipFile("testzip.zip", "w") as newzip: # creates a context manager
        newzip.write("newfile.txt")
        newzip.write("textfile.txt.bak")
        # when the two lines above finish executing, 
        # the with statement will automatically close the zip file