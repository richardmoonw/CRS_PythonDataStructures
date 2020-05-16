# Exercise: Take the following Python code that stores a string:

# str = 'X-DSPAM-Condifence: 0.8475 '

# Use find and string slicing to extract the portion of the string 
# after the colon character and then use float function to convert
# the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
piece = str[ipos+2:]
print(piece)