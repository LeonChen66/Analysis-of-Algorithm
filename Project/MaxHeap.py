class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)
    
    def heapify(self):
        n = len(self.heap) - 1
        self.__bubbleDown(1)
        # start at last parent and go left one node at a time
        # for i in range(n//2, -1, -1):
        #     self.__bubbleDown(i)

    def empty(self):
        return len(self.heap)==1

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def delete(self,w):
        for i in range(1,len(self.heap)):
            a,b = self.heap[i]
            if b==w:
                break
        del self.heap[i]
        self.heapify()

    def pop(self):
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
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)


if __name__ == "__main__":
    m = MaxHeap()
    m.push((1, 2))
    m.push((2, 2))
    m.push((4, 3))
    m.push((5, 4))
    m.delete(4)
    print(m.heap)
