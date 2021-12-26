"""
8.4 Open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to
see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

myList = list()                         # Empty list
fname = input("Enter file name: ")      # Gets filename, but NOT the data itself
fh = open(fname)                        # The data
# lst = list()
for line in fh:                         # Gets each line
    splitLines = line.split()           # Splits the lines
    # print(splitLines)                 # Prints them

    # This section is a nested loop to check both splitLines and myList
    # I am using 'not in' because it is the easiest way to do it (I think)
    for val in splitLines:
        if val not in myList:
            myList.append(val)      # Appending the list as required

myList.sort()                           # Puts list into alphabetical order
print(myList)
# for word in splitLines:
#     myList.append(word)
