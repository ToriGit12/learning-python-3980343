# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing (open()) and create it if it doesn't exist ("w+")
# sample_file = open("textfile.txt", "w+")
# # Write some data to the file
# sample_file.write("This is some sample text in our sample file.")
# sample_file.write("Some more sample text.")
# # Now close it
# sample_file.close()

# Open the file for appending text to the end ("a+")
sample_file = open("textfile.txt", "a+")

# write some lines of data to the file
sample_file.write("Some more sample text.")
sample_file.write("Even more sample text.")

# close the file when done
sample_file.close()