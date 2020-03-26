class Node(object):

    def __init__(self, value = None, color = None):
        self.__value = value
        self.__color = color

        self.__left = None
        self.__right = None
        self.__parent = None

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,value):
        return self.__value = value

    @property
    def color(self):
        return self.__color   

    @color.setter
    def color(self,color):
        self.__color = color

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
    def right(self,right):
        self.__right = right

    @property
    def parent(self):
        return self.__parent
    
    @parent.setter
    def parent(self,parent):
        self.__parent = parent
    
    def is_black(self):
        return self.color == "b"

    def mark_as_red(self):
        self.color = "r"
    
    def mark_as_black(self):
        self.color = "b"

    @staticmethod
    def generate_red_node(self,value):
        return Node(value,'r')

    @staticmethod
    def generate_black_node(self,value):
        return Node(value,'b')


class RedBlackTree(object):
    def __init__(self):
        self.__root = None
        self.__null_leaf = Node(color='b')
    
    @property
    def root(self):
        return self.__root
    
    @root.setter
    def root(self,root):
        self.__root = root

    @property
    def null_leaf(self):
        return self.__null_leaf

    @null_leaf.setter
    def null_leaf(self,null_leaf):
        self.__null_leaf = null_leaf

    def insert(self,value):

        new_node = Node.generate_red_node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node != self.null_leaf:
                point = current_node
                if value < current_node.value:
                    current_node = current_node.left
                elif value > current_node.value:
                    current_node = current_node.right
                else:
                    point = None
                    break
        
        if point is None:
            return
        if value < point.value:
            point.left = new_node
        else:
            point.right = new_node
        
        new_node.parent = point

        new_node.left = new_node.right = self.null_leaf

        self._self_balance(new_node)

    
    def _self_balance_after_insert(self,node):
        pass

    def delete(self,value):
        pass

    def _self_balance_after_delete(self,node):
        pass

    def _left_rotate(self,node):
        pass

    def _right_rotate(self,node):
        pass
    
    def _parent(self,node):
        pass

    def _uncle(self,node):
        pass

    def _grandfather(self,node):
        pass

    


                    
                    

