class CircleQueue(object):

    def __init__(self,queue_size = 0):
        self.__queue_size = queue_size
        self.__queue = [0] * queue_size 
        self.__head = self.__tail = 0
    
    def enqueue(self, value):
        #queue is full
        if (self.__tail + 1) % self.__queue_size == self.__head:
            return

        self.__queue[self.__tail] = value;
        self.__tail = (self.__tail + 1) % self.__queue_size
        
    def dequeue(self):

        #queue is empty
        if self.__tail == self.__head:
            return
        element = self.__queue[self.__head]
        self.__head = (self.__head + 1) % self.__queue_size
        return element

    def size(self):
        return (self.__tail - self.__head + self.__queue_size) % self.__queue_size

    def __str__(self):
        return " ===> ".join(str(item) for item in  self.__queue)

if __name__ == '__main__':
    circle_queue = CircleQueue(5)

    for item in range(0 , 10):
        circle_queue.enqueue(item)

    print(circle_queue)

    for _ in range(0,10):
        print(circle_queue.dequeue())
    