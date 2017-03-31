class Heap(object):
    HEAP_SIZE = 10                                              # Define Heap Size

    def __init__(self):
        self.heap = [0]*(self.HEAP_SIZE)                        # Initialize an empty array with "0's"
        self.currentPosition = -1                               # Points to Index of 1-D Array

    # Insert an item into the Heap
    def insert(self,item):
        # Check if Heap is Full
        if self.isFull():
            print('Heap is Full..')
            return
        # If Heap not Full, increment the currentPosition Pointer
        self.currentPosition += 1
        # Insert the item in the Heap (array)
        self.heap[self.currentPosition] = item
        # On every insertion, see that Heap Properties are not violated
        self.fixUp(self.currentPosition)


    # If Heap is Full i.e the Pointer "currentPosition" is equal to "HEAP_SIZE" i.e last item
    # Return True else False
    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False


    # Funtion to make sure that Heap Properties are Valid or else fix it up
    # Property: Largest Item must be at the Root Node
    def fixUp(self, index):
        # Find the Parent Index (i) for child nodes (2i+1) and (2i+2)
        parentIndex = int((index-1)/2)
        # On insertion of a new item, see if the parent item is smaller than its child node
        # If so, swap the two items and check this property till the root node.
        while (parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]):
            temp = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[index]
            self.heap[index] = temp
            # Keep iterating till we bump into the Root Node
            parentIndex = (int)((index-1)/2)


    # Heap Sort Function
    def heapSort(self):
        for i in range(0,self.currentPosition+1):
            # In a Max. Heap, the Maximum value is at the Root
            temp = self.heap[0]
            print('%d' % temp)
            # Swap the Max item i.e root node with the Largest Occupied Index (currentPosition) in Heap
            # Keep Doing this till all items are Sorted
            self.heap[0] = self.heap[self.currentPosition-i]
            self.heap[self.currentPosition-i] = temp
            # Fix the Heap to be Valid and check the Max. Property
            # fixDown(StartIndex, StopIndex)
            self.fixDown(0,self.currentPosition-i-1)


    # Function to Fix the Heap Max. Root Property for Heap Sort
    def fixDown(self, index, upto):
        while index <= upto:
            leftChild = (2*index+1)
            rightChild = (2*index+2)
            # If index of Left Child is smaller that Upto index
            # ex. currentIndex = 8, leftChild = 1; "1 < 8"
            if leftChild < upto:
                childToSwap = None
                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    # If value of Left Child is greater than Right Child value
                    # Swap with Left Child else Right Child
                    if (self.heap[leftChild] > self.heap[rightChild]):
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if (self.heap[index] < self.heap[childToSwap]):
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break
                index = childToSwap
            else:
                break


# -------------------- Testing ----------------------
if __name__ == '__main__':

    heap = Heap()
    heap.insert(10)
    heap.insert(-20)
    heap.insert(0)
    heap.insert(2)

    heap.heapSort()

# ------------------------------------ EOC ------------------------------