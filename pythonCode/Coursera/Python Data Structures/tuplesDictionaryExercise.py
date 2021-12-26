"""
This is some code to try and get a better understanding of data structures
"""

fhand = open("romeo.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1 # This gets histogram values

# Extracts information from dictionary and makes a reverse tuple i.e. (val,Key)
# instead of (key,val)
lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst,reverse=True) # reverse=True sots backwards, from highest to low

for val,key in lst[:10]:
    print(key,val)

# Notice how the (key, val) is flipped a few times throughout the process, as
# required
