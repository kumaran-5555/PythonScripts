__author__ = 'serajago'

#http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

l = [3, 34, 4, 12, 5, 2]
sum = 9

dpTable = []
for i in range(l, len(l)):
    dpTable.append([sum]*len(l))


dpTable[i][j] =
