"""
9.4 Write a program to read through the mbox-short.txt and figure out who
has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those
lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary
using a maximum loop to find the most prolific committer.
"""

mailSender = dict()
count = 0
name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    count = count + 1
    senderNames = line.split()
    # print(splitLines[1])
    # print(senderNames[1])

    #if senderNames[1] not in mailSender:
    if senderNames[1] not in mailSender:
        mailSender[senderNames[1]] = 1
    else:
        mailSender[senderNames[1]] = mailSender[senderNames[1]] + 1


# So, now all histograms have been totalled, I need to find the biggest one
bigCount = None
bigEmail = None
for senderNames,mailSender in mailSender.items():
    if bigCount is None or mailSender > bigCount:
        bigCount = mailSender
        bigEmail = senderNames

print(bigEmail,bigCount)
