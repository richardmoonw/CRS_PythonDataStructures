# Exercise: Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

# Open a the file and create a dictionary
file = open("files/mbox-short.txt", "r")
hours = dict()

# Iterate over each line of the file and evaluate those that starts with a "From" and are greater than 5 in length
for line in file:

    words_list =  line.split()
    if words_list != [] and len(words_list) > 5:
        if words_list[0] == "From":
            time = words_list[5]

            # Get the hour in which each email was sent
            time_details = time.split(":")
            hour = time_details[0]

            hours[hour] = hours.get(hour, 0) + 1

# Convert the dictionary in a list of tuples and sort it by value. (List Comprehension)
sorted_hours = sorted([ (hour, emails_sent) for hour, emails_sent in hours.items() ])

# Print the hours and the number of emails sent in it 
for hour, emails_sent in sorted_hours:
    print(hour, emails_sent)