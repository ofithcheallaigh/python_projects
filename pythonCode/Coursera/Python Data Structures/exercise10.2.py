"""
10.2 Write a program to read through the mbox-short.txt and figure
out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and
then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 (interested in the 09)
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
"""
distribution = dict()
count = 0
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    count = count + 1
    firstSplit = line.split()           # This gets me the line of text
    # print(firstSplit)
    time = firstSplit[5]                # This gets me time - ex: 09:11:38
    # print(time)
    timeSplit = time.split(':')
    hr = timeSplit[0]                   # This gets me hrs - ex: 09
    # print(hr)   
    # print(hr)

    # Gets me the histogram
    if hr not in distribution:
    # if not (hr in list(distribution.keys())):
        distribution[hr] = 1
    else:
        distribution[hr] = distribution[hr] + 1
# print(distribution)

sortedDistribution = sorted(distribution.items())
for distribution, hr in sortedDistribution:
    print(distribution,hr)

