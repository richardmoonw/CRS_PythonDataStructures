# Exercise: Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end. Hint: make sure not to include the lines that start with 'From:'.

# Ask the user for a file name
fname = input()

# Open the file
file = open(fname, "r")
emailList = list()

# Look in every line of the file that starts with "From" and does not with "From:"
for line in file:

        # Ignore all the blank lines
        if line == '\n':
            continue

        # Split the line, verify if it starts with "From", get the email address and append it to the list
        splittedLine = line.split()
        if len(splittedLine) < 2 or splittedLine[0] != "From": 
            continue
        emailAddress = splittedLine[1]
        print(emailAddress)
        emailList.append(emailAddress)

# Return the number of emails got
print("There were", len(emailList), "lines in the file with From as the first word")