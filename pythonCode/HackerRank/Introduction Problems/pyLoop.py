"""
Task
    Read an integer N. For all non-negative integers i < N, print i^2. See the
    sample for details

Input format
    The first and only line contains the integer, N.

Constraints
    1 <= N <= 20

Output format
    Print N lines, one corresponding to each i

Sample Input
    5

Sample Output
    0
    1
    4
    9
    16
"""

n = int(input())    # Asks for input
num = range(n)      # Cannot loop over int, go converts int to a range
for i in (num):     # For loop to loop over range
    print(i*i)      # Simple way to get square of number
