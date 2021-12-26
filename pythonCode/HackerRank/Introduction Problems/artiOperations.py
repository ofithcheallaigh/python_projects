"""
Task
Read two integers from STDIN and print three lines where:
    1. The first line contains the sum of the two numbers.
    2. The second line contains the difference of the two numbers (first - second).
    3. The third line contains the product of the two numbers

Input format
    The first line contains the first integer, . The second line contains the second integer, b.

Contstraints
    1 <= a <= 10^10
    1 <= b <= 10^10

Output format
    Print the three lines as explained above

Sample Input
    3
    2

Sample Output
    5
    1
    6

Explanation
    3 + 2 = 5
    3 - 2 = 1
    3 * 2 = 6
"""

a = int(input())
b = int(input())
addNums = a + b
subNums = a - b
mulNums = a * b

print(addNums)
print(subNums)
print(mulNums)
