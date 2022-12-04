class Stack:
    __slots__ = ['__size', '__top']


    def __init__(self):
        self.__top = []
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def push(self, value):
        self.__top.append(value)
        self.__size += 1

    def pop(self):
        if not self.is_empty():
            element = self.__top.pop()
            self.__size -= 1
            return element
        return None
    
    def peek(self):
        return self.__top[-1]

    def __str__(self):
        return str(self.__top)