l = [ 10,12,3,4,56,7,0,8,9,11,12]
l=[0,1,2,3,4,5,-1]
class MergeSort():
    def __init__(self, listToSort):
        self.listToSort = listToSort
        self.tempList = []
        for i in self.listToSort:
            self.tempList.append(-1)

    def __str__(self):
        return str(self.listToSort)

    def mergeList(self, left, leftEnd, rightStart, right):
        cursor = left
        leftCursor = left
        rightCursor = rightStart
        while cursor <= right:
            if self.listToSort[leftCursor] < self.listToSort[rightCursor]:
                self.tempList[cursor] = self.listToSort[leftCursor]
                leftCursor+=1
                cursor+=1
            elif self.listToSort[leftCursor] > self.listToSort[rightCursor]:
                self.tempList[cursor] = self.listToSort[rightCursor]
                rightCursor+=1
                cursor+=1





    def mergeSort(self, left, right):
        """

        :rtype : object
        """
        pivot = left + (right-left)/2

        if left < right:
            # split
            self.mergeSort(left, pivot)
            self.mergeSort(pivot+1, right)

q = QuickSort(l)
q.testQuickSort(0,len(l)-1)
print(q.listToSort)
print(QuickSort.quickSort.__doc__)