# Exercise: Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it 
# to the list. When the program completes, sort and print the resulting words in alphabetical order.

# Ask the user for a file name
fname = input()

# Open the file
romeo = open("files/" + fname, "r")
wordsList = list()

# Split every line of the document
for line in romeo:
    line_words_list = line.rstrip().split()

    # Check if a word is already in the list, and if not append it
    for word in line_words_list:
        if word not in wordsList:
            wordsList.append(word)

wordsList.sort()
print(wordsList)