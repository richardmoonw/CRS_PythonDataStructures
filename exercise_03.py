# Exercise: Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# Ask for the file name
fname = input()

# Open the file with the given name
fhandler = open("files/" + fname, "r")

# Print the content of the file in upper case
file_content = fhandler.read().strip()
print(file_content.upper())