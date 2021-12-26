"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch
it with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
"""
largestNum = None
smallestNum = None
total = 0.0
num = 0
# largestNum = -1
while True:
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        fval = int(sval)
    except:
        print("Invalid Input")
        continue
    # Below is used to find the largest number
    if largestNum is None:
        largestNum = fval
    elif fval > largestNum:
        largestNum = fval
    # Below is used to find the smallest number
    if smallestNum is None:
        smallestNum = fval
    elif fval < smallestNum:
        smallestNum = fval

# print("Invalid Input")
print("Maximum is", largestNum)
print("Smallest is", smallestNum)
