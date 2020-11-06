# MaxHeap - binary tree with each layer full filled left to right
# every node is lower than or equal to layer above it
# Insert: O(logn)
# Get Max in O(1)
# Remove Max in O(logn)
# Quick because the max is the number 1.
# Easy to implement using an array

# to find:
# parent(i) = i / 2
# left(i) = i * 2
# right(i) = i * 2 + 1

# push = insert - add to array at bottom of heap and float it up
# peek = get max - swap with last value in heap at bottom right, delete it, save it as max value, then bubble down the swapped
# pop = remove max


# constructor may receive a list of items to insert into heap
class MaxHeap:
    def __init__(self, items=[]):
        # create new list with 0 in it
        self.heap = [0] # 0 is not being used
        # append to list any items that were passed in
        for i in items:
            self.heap.append(i)
            # float up to the right position
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        # receive a piece of data, appending to end of heap
        self.heap.append(data)
        # float it up to its proper position
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        # checks if we at least have 1 value in the heap
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        # 1. there are more than 2 values in the heap
        # then swap max value to end of heap before floating down swapped value
        # 2. there's only 1 value in heap, just pop off
        # 3. pop off an empty heap, where we just return false.
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        # if the value of the item is greater than its parent
        elif self.heap[index] > self.heap[parent]:
            # swap the two and float it up
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index): # sometimes called Max Heapify
        left = index * 2
        right = index * 2 + 1
        largest = index
        # compare our index value to the left child and to the right child
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left # index of the largest, not the value
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            # if we found the largest and the largest is not the index
            self.__swap(index, largest) # swap places
            self.__bubbleDown(largest) # call recursively to keep bubbling down

m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))