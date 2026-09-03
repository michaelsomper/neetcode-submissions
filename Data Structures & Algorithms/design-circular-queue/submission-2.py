class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * self.size
        self.front = 0
        self.rear = 0
        self.elements = 0

    def enQueue(self, value: int) -> bool:
        print(self.queue)
        if self.elements != self.size:
            # print("Ran enqueue function")
            # print("rear: " + str(self.rear))
            if self.elements != 0:
                self.queue[(self.rear + 1) % self.size] = value
                self.rear = (self.rear + 1) % self.size
            else:
                self.queue[self.rear] = value
            self.elements += 1
            # print(str(self.rear))
            return True
        else:
            print("Failed")
            return False

    def deQueue(self) -> bool:
        if self.elements != 0:
            self.front = (self.front + 1) % self.size
            self.elements -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.elements != 0:
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        print(self.rear)
        print(self.queue)
        if self.elements != 0:
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        if self.elements == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.elements == self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()