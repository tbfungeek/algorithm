class AVLNode(object):

    def __init__(self,data):
        self.__left = None
        self.__right = None
        self.__data = data
        self.__height = 0
        self.__balance = 0

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

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        self.__height = height

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        self.__balance = balance

    def __str__(self):
        return "data = {} height = {} balance = {}".format(self.data,self.height,self.balance)

class AVLTree(object):
    
    def __init__(self):
        self.__root = None
    
    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self,root):
        self.__root = root
    
    def __insert(self,data,root):
        if root is None:
            root = AVLNode(data)
            return root
        elif  data == root.data:
            return root
        elif data < root.data:
            #print("insert {} as left node root data {}".format(data,root.data))
            root.left = self.__insert(data,root.left)
        else:
            #print("insert {} as right node root data {}".format(data,root.data))
            root.right = self.__insert(data,root.right)
        return root

    def rebalance(self):

        self.update_height_and_balance()
        if self.root.balance > 1:
            if self.root.left.balance > 0:
                #print("ll {} as balance {}".format(data,root.balance))
                self.root = self._ll_rotation(self.root)
            else:
                #print("lr {} as balance {}".format(data,root.balance))
                self.root = self._lr_rotation(self.root)
        elif self.root.balance < -1:
            if self.root.right.balance > 0:
                #print("rl {} as balance {}".format(data,root.balance))
                self.root = self._rl_rotation(self.root)
            else:
                #print("rr {} as balance {}".format(data,root.balance))
                self.root = self._rr_rotation(self.root)

        

    def insert(self,data):
        self.__root = self.__insert(data,self.__root)
        self.rebalance()

    def update_height_and_balance(self):
        self.update_nodes_height()
        self.update_nodes_balance()

    def delete(self,data):
        pass

    #        x                
    #       / \             
    #      z   D            
    #     / \         
    #    y   C
    #   / \ 
    #  A   B
    def _ll_rotation(self,sub_tree_root):
        new_root = sub_tree_root.left
        sub_tree_root.left = new_root.right
        new_root.right = sub_tree_root
        self.update_height_and_balance()
        return new_root

    #        y
    #       / \
    #      A   z
    #     / \
    #    B   x
    #   / \
    #  C   D
    def _rr_rotation(self,sub_tree_root):
        new_root = sub_tree_root.right
        sub_tree_root.right = new_root.left
        new_root.left = sub_tree_root
        self.update_height_and_balance()
        return new_root

    #        x              
    #       / \  
    #      y   D 
    #     / \      
    #    A   z        
    #       / \       
    #      B   C  
    def _lr_rotation(self,sub_tree_root):
        sub_tree_root.left = self._rr_rotation(sub_tree_root.left)
        return self._ll_rotation(sub_tree_root)
        
    #     y              
    #    / \    
    #   A   x   
    #      / \   
    #     z   D  
    #    / \    
    #   B   C   
    def _rl_rotation(self,sub_tree_root):
        sub_tree_root.right = self._ll_rotation(sub_tree_root.right)
        return self._rr_rotation(sub_tree_root)

    def update_node_height(self,node):
        if node is None:
            return  0
        else:
            if node.left is None:
                node_left_height = 0
            else:
                node_left_height = self.update_node_height(node.left)
                node.left.height = node_left_height
                
            if node.right is None:
                node_right_height = 0
            else:
                node_right_height = self.update_node_height(node.right)
                node.right.height = self.update_node_height(node.right)
            return  max(node_left_height,node_right_height) + 1

    def update_node_balance(self,node):
        if node:
            node.balance = self.node_height(node.left) - self.node_height(node.right)
            if node.left:
                self.update_node_balance(node.left)
            if node.right:
                self.update_node_balance(node.right)
        else:
            node.balance = 0

    def node_height(self,node):
        if node is None:
            return 0
        else:
            return node.height
    
    def update_nodes_height(self):
        if self.root: 
            if self.root.left: 
                self.root.left.height = self.update_node_height(self.root.left)
            if self.root.right:
                self.root.right.height = self.update_node_height(self.root.right)
            self.root.height = self.update_node_height(self.root)
        else: 
            self.root.height = 0

    def update_nodes_balance(self):
        self.update_node_balance(self.root)

    def preOrderTravel(self):
        return self.__preOrderStack(self.root)

    def __preOrderStack(self,node):
        if node is None:
            return
        stack = []
        current_node = node
        while current_node or len(stack) > 0:
            while current_node:
                stack.append(current_node)
                yield current_node
                current_node = current_node.left
            current_node = stack.pop()
            current_node = current_node.right

if __name__ == "__main__":
    avltree = AVLTree()
    avltree.insert(43)
    avltree.insert(18)
    avltree.insert(22)
    avltree.insert(9)
    avltree.insert(21)
    avltree.insert(6)
    
    for item in avltree.preOrderTravel():
        print(item)

        



    
        
    
