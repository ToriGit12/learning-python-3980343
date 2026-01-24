#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path # we are calling a submodule here
import time
from datetime import datetime

# Print the name of the OS (the operating system that I am running on)
print(os.name)

# Check for item existence and type
print("Item exists:", path.exists("textfile.txt"))
print("Item is a file:", path.isfile("textfile.txt"))
print("Item is a directory:", path.isdir("textfile.txt"))

# Work with file paths
print("Item's path:", path.realpath("textfile.txt"))
print("Item's path and name:", path.split(path.realpath("textfile.txt")))

# Get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print(t)

# Operating system has a timestamp that's on each file,
# but it is in milliseconds; fromtimestamp gives readable time
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

# Calculate how long ago the item was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
print(f"It has been {td} since the file was modified.")
print(f"Or {td.total_seconds()} seconds")