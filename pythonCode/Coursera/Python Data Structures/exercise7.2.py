"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

# Use the file name mbox-short.txt as the file name
count = 0
fullCount = 0
totalNum = 0

fname = input("Enter file name: ")

fh = open(fname)
for line in fh:
    # fullCount = fullCount + 1
    if not line.startswith("X-DSPAM-Confidence:") :
        continue                # If the line doesn't start with above, continue
    # print(line)               # Prints out each line
    count = count + 1           # This will count the number of lines printed

    firstPos = line.find("0")
    fullText = line[firstPos:]
    initialNum = float(fullText)

    totalNum = totalNum + initialNum

print("Average spam confidence:", totalNum/count)

