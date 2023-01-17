#9.4 Write a program to read through the mbox-short.txt and figure out who has
#sent the greatest number of mail messages. The program looks for 'From ' lines
#and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address
#to a count of the number of times they appear in the file. After the
#dictionary is produced, the program reads through the dictionary using
#a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
handle = open(fname)

counts = dict()
lst = list()
for line in handle:
    #line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    words = words[1]
    #appending the list with all the email addresses
    lst.append(words)
# counting the occurence of each email address in the list

for name in lst:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

#looking for the word with the maximum count
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
