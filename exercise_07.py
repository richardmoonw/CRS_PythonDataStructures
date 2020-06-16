# Exercise: Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates 
# a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the 
# dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Open the file and declare the new dictionary
file = open("files/mbox-short.txt", "r")
persons = dict()

# Iterate over each line of the file and find the number of emails sent by each user
for line in file:

    words_in_line = line.split()
    if words_in_line != [] and len(words_in_line) > 1:
        if words_in_line[0] == "From":
            sender = words_in_line[1]
            persons[sender] = persons.get(sender, 0) + 1
        

# Find the person who has sent the maximum number of emails
best_sender = None
maximum_emails = None
for sender, emails_sent in persons.items():
    if best_sender == None or emails_sent > maximum_emails:
        best_sender = sender 
        maximum_emails = emails_sent

print(best_sender, str(maximum_emails))