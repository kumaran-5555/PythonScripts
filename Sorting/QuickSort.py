l = [ 10,12,3,4,56,7,0,8,9,11,12]
class QuickSort():
    def __init__(self, listToSort):
        self.listToSort = listToSort
    def __str__(self):
        return str(self.listToSort)

    def quickSort(self, left, right):
        """

        :rtype : object
        """
        if left < right:

            pivotIdx=int(left+((right-left)/2))
            pivotNewIdx=pivotIdx
            i=left
            j=right
            pivot=self.listToSort[pivotIdx]
            while(i<j):
                while (self.listToSort[i]<=pivot and i<right):
                    i=i+1
                while(self.listToSort[j] > pivot):
                    j=j-1
                if(i<j):
                    if(i==pivotIdx):
                        pivotNewIdx=j
                    elif(j==pivotIdx):
                        pivotNewIdx=i

                    temp=self.listToSort[i]
                    self.listToSort[i]=self.listToSort[j]
                    self.listToSort[j]=temp
            temp=self.listToSort[pivotNewIdx]
            self.listToSort[pivotNewIdx] = self.listToSort[j]
            self.listToSort[j]=temp
            self.quickSort(left,j-1)
            self.quickSort(j+1,right)








q = QuickSort(l)
print(q)
q.quickSort(0,len(l)-1)
print(q)


print(QuickSort.quickSort.__doc__)