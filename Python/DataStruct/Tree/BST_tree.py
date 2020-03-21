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

        if self.data is None:
            self.data = value
            return

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

    def height(self):
        return self.tree_height(self)

    def tree_height(self,node):
        if node is None:
            return 0
        return max(self.tree_height(node.left),self.tree_height(node.right)) + 1

    def delete(self,value):
        current_node = self
        parent = None
        #find the node
        while current_node and current_node.data != value:
            parent = current_node
            current_node = current_node.left if current_node.data > value else current_node.right
        if current_node is None:
            return
        
        #in case of the node has left child and right child
        if current_node.left is not None and current_node.right is not None:
            successor = current_node.right
            successor_parent = current_node
            
            #find the item next to current node in inOrder
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            #replace current node with value next to current node in inOrder
            current_node.data = successor.data
            #it will be delete later
        
        #begin to process the case of only has one child
            parent , current_node = successor_parent , successor

        child = None
        #in case of only has left child
        if current_node.left is not None:
            child = current_node.left
        #in case of only has right child
        elif current_node.right is not None:
            child = current_node.right
        
        #delete item 
        if parent is None:
            self = child
        if parent.left == current_node:
            parent.left = child
        else:
            parent.right = child

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
        if self.data is None: 
            return
        if self.left is not None:
            yield from self.left.inOrderTraverl()
        yield self.data
        if self.right is not None:
            yield from self.right.inOrderTraverl()
    
    def inOrderStack(self):
        if self.data is None:
            return
        stack = []
        node = self
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.data
            node = node.right

    def preOrderTravel(self):
        if self.data is None: 
            return
        yield self.data
        if self.left is not None:
            yield from self.left.preOrderTravel()
        if self.right is not None:
            yield from self.right.preOrderTravel()

    def preOrderStack(self):
        if self.data is None:
            return
        stack = []
        node = self
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                yield node.data
                node = node.left
            node = stack.pop()
            node = node.right

    def postOrderTravel(self):
        if self.data is None: 
            return
        if self.left is not None:
            yield from self.left.postOrderTravel()
        if self.right is not None:
            yield  from self.right.postOrderTravel()
        yield self.data

    def postOrderStack(self):
        if self.data is None:
            return
        stack1 = []
        stack2 = []
        stack1.append(self)
        while len(stack1) > 0:
            node = stack1.pop()
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
            stack2.append(node)
        
        while len(stack2) > 0:
            yield stack2.pop().data

    def leaveOrderTravel(self):
        if self.data is None: 
            return
        queue = []
        queue.append(self)
        while queue:
            node = queue.pop(0)
            yield node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)    

if __name__ == "__main__":

    binary_tree = BSTree(5)
    binary_tree.insert(3)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(2)
    binary_tree.insert(6)
    binary_tree.insert(9)
    binary_tree.insert(10)
    #print(binary_tree.contain(10))

    print(binary_tree.height())

    #for data in binary_tree.inOrderTraverl():
    #    print(data)

    #print("="*50+">")

    #for data in binary_tree.preOrderTravel():
    #    print(data)
    
    #print("="*50+">")

    #for data in binary_tree.postOrderTravel():
    #    print(data)

    binary_tree.delete(10)
    
    print(binary_tree.height())

    #for data in binary_tree.leaveOrderTravel():
    #    print(data)

    #for data in binary_tree.postOrderStack():
    #    print(data)

    print("="*50+">")
