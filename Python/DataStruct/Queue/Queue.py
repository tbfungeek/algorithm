
class Node(object):
    def __init__(self,data,next=None):
        self.__data = data
        self.__next = next
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    def __str__(self):
        return str(self.__data)


class Queue(object):
    
    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self,value):
        pass

    def dequeue(self):
        pass

    def __str__(self):
        pass

    def __iter__(self):
        pass
    
    def size(self):
        pass

if __name__ == '__main__':
    pass

    