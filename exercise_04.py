# Exercise: Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute the average of those values 
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Ask the user for a file name
fname = input()

# Open the file
fhandler = open("files/" + fname, "r")

# Read through the file, look for matches, count the lines and extract the values
counter = 0
numbers = []
for line in fhandler:
    if 'X-DSPAM-Confidence' in line:
        numbers.append(line[21:-1])
        counter += 1

# Compute the average
total = 0.0
for number in numbers:
    total = total + float(number)
total = total/counter
print("Average spam confidence:", total)