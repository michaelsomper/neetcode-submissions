from collections import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_length = 0
        self.min_stack = []
        self.min_stack_length = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_length += 1
        if not self.min_stack or (self.min_stack and val <= self.min_stack[self.min_stack_length - 1]):
            self.min_stack.append(val)
            self.min_stack_length += 1

    def pop(self) -> None:
        if self.stack:
            if self.min_stack[self.min_stack_length - 1] == self.stack[self.stack_length - 1]:
                self.min_stack_length -= 1
                self.min_stack.pop()
            self.stack_length -= 1
            self.stack.pop()

    def top(self) -> int:
        return self.stack[self.stack_length - 1]

    def getMin(self) -> int:
        return self.min_stack[self.min_stack_length - 1]
