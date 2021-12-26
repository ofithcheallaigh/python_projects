"""
Read an integer N.
Without using any string methods, try to print the following:
    123...N
Note that "..." represents the values in between.

Input format
    The first line to contain an integer, N.
Output format
    Output the answer as explained in the task
Sample Input
    3
Sample Output
    123
"""

n = int(input())
# num = range()
for num in range(n):        # Need to get n, a single number, into a range
    # The end='' gets the numbers printed horizontally
    # Also, num+1 means we drop the zero, and go one
    # past the 'up to, but not including' thing for range
    print(num+1, end='')
