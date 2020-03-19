class BSTree(object):

    def __init__(self,data):
        self.__data  = data
        self.__left  = None
        self.__right = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,data):
        self.__data = data

    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self,left):
        self.__left = left

    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, right):
        self.__right = right

    def __str__(self):
        return str(self.__data)

    def insert(self,value):
        if value <= self.data:
            if self.left is None:
                self.left = BSTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTree(value)
            else:
                self.right.insert(value)

    def contain(self,value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contain(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contain(value)


    def inOrderTraverl(self):
        if self.left is not None:
            yield from self.left.inOrderTraverl()
        yield self.data
        if self.right is not None:
            yield from self.right.inOrderTraverl()

    def preOrderTravel(self):
        yield self.data
        if self.left is not None:
            yield from self.left.preOrderTravel()
        if self.right is not None:
            yield from self.right.preOrderTravel()

    def postOrderTravel(self):
        if self.left is not None:
            yield from self.left.postOrderTravel()
        if self.right is not None:
            yield  from self.right.postOrderTravel()
        yield self.data 

if __name__ == "__main__":

    binary_tree = BSTree(10)
    binary_tree.insert(5)
    binary_tree.insert(15)
    binary_tree.insert(8)
    print(binary_tree.contain(10))

    for data in binary_tree.inOrderTraverl():
        print(data)

    print("="*50+">")

    for data in binary_tree.preOrderTravel():
        print(data)
    
    print("="*50+">")

    for data in binary_tree.postOrderTravel():
        print(data)
