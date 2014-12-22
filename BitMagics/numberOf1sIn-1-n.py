#!/usr/bin/python
__author__ = 'serajago'

n = 32
maxBits = 64
count = [0] * maxBits

# count[i] - holds number of 1's in all the numbers that can be generated before setting i th bit as 1 plus 1

def getNumberOf1S(n):
    # find the left most 1 bit
    len(bin(n)[2:])
    # base case
    count[0] = 1
    count[1] = 2
    for i in range(2, maxBits):
        count[i] = count[i-1] + count[i-1] + (pow(2,i-1)-1)

getNumberOf1S(n)
print(count)
