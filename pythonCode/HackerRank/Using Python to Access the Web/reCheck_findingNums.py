import re
hand = open("regex_sum_13211.txt")
"""for line in hand:
    y = re.findall('[0-9]+', line)
print(y)"""
mySum = 0
for line in hand:
    y = re.findall('[0-9]+', line)
    nums = [int(x) for x in y]
    print(nums)
    for myNum in nums:
        mySum = mySum + myNum
        print(mySum)
