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
        self.__value = value

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

    def is_red(self):
        return self.color == "r"

    def mark_as_red(self):
        self.color = "r"
    
    def mark_as_black(self):
        self.color = "b"

    @staticmethod
    def generate_red_node(value):
        return Node(value,'r')

    @staticmethod
    def generate_black_node(value):
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

    def find(self, key, node):
        if self.root is None:
            return None
        elif not node:
            return Node
        elif key < node.value:
            return self.find(key,node.left)
        elif key > node.value:
            return self.find(key,node.right)
        else:
            return node

    def findMin(self, node):
        current_node = node
        while current_node.left is not self.null_leaf:
            current_node = current_node.left
        return current_node

    def findMax(self, node):
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def insert(self,value):

        new_node = Node.generate_red_node(value)
        point = None
        #新节点N位于树的根上，没有父节点
        if self.root is None:
            #我们把它重绘为黑色
            new_node.left = new_node.right = self.null_leaf
            self.root = new_node
            self.root.mark_as_black()
            return
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
        
        if point is not None:
            if value < point.value:
                point.left = new_node
            else:
                point.right = new_node
            new_node.parent = point
            new_node.left = new_node.right = self.null_leaf
        self._self_balance_after_insert(new_node)
    
    def _self_balance_after_insert(self,node):

        current_node = node
        #current_node.parent.is_black() 新节点的父节点P是黑色,在这种情形下，树仍是有效的
        while current_node is not self.root and not current_node.parent.is_black():
            parent = self._parent(current_node)
            uncle  = self._uncle(current_node)
            grandfather = self._grandfather(current_node)

            if uncle is not None and uncle.is_red():
                parent.mark_as_black()
                uncle.mark_as_black()
                grandfather.mark_as_red()
                #但是，这种情况红色的祖父节点可能是根节点，这就违反了根结点只能是黑色结点的规则
                #为了解决这个问题，我们在祖父节点上递归地进行情形1的整个过程
                current_node = grandfather
                continue
            
            #但凡能到这里都满足两个条件，叔结点是黑色或者没有，父亲结点是红色
            if parent == grandfather.left:
                if current_node == parent.right:
                    #叔节点是黑色或缺少，并且新节点是其父节点的右子节点而父节点又是其父节点的左子节点。
                    #这种情形下，我们进行一次左旋转调换新节点和其父节点的角色
                    self._left_rotate(parent)
                    #让node指向原先的parent
                    current_node = current_node.left
                    #同时更新parent，uncle，grandfather
                    parent = self._parent(current_node)
                    uncle  = self._uncle(current_node)
                    grandfather = self._grandfather(current_node)

                parent.mark_as_black()
                grandfather.mark_as_red()
                self._right_rotate(grandfather)

            elif parent == grandfather.right:
                if node == parent.left:
                    self._right_rotate(parent)
                    current_node = current_node.right
                    parent = self._parent(current_node)
                    uncle  = self._uncle(current_node)
                    grandfather = self._grandfather(current_node)
                parent.mark_as_black()
                grandfather.mark_as_red()
                self._left_rotate(grandfather)

        self.root.mark_as_black()

    def delete(self,value):
        self._delete(self.find(value,self.root))

    def _delete(self,node):

        if self.root is None or node is None:
            return
        #记录删除结点的颜色
        delete_node_color = node.color
        #当要删除的结点是单结点的情况
        if node.left is self.null_leaf:
            temp_node = node.right
            self._transplant(node,node.right)
        elif node.right is self.null_leaf:
            temp_node = node.left
            self._transplant(node,node.left)
        else:
            min_node = self.findMin(node.right)
            delete_node_color = min_node.color
            temp_node = min_node.right
            if min_node.parent != node:
                #删除最小的结点
                self._transplant(min_node, min_node.right)
                min_node.right = node.right
                min_node.right.parent = min_node
            self._transplant(node,min_node)
            min_node.left = node.left
            min_node.left.parent = min_node
            min_node.color = node.color
        
        if self.root == self.null_leaf:
            self.root = None
            return 

        if delete_node_color == 'b':
            self._self_balance_after_delete(temp_node)

    def _self_balance_after_delete(self,node):
        #如果当前待删除节点是红色的，它被删除之后对当前树的特性不会造成任何破坏影响。
        if node is self.null_leaf:
            return 
        current_node = node
        while current_node != self.root and current_node.is_black():
            parent = self._parent(current_node)
            brother = self._brother(current_node)
            uncle  = self._uncle(current_node)
            grandfather = self._grandfather(current_node)

            #删除的节点是黑色，他的兄弟节点是红色
            if brother.is_red():
                #把兄弟搞成黑的
                brother.mark_as_black()
                #父亲搞成红的
                parent.mark_as_red()
                #左旋转父亲
                self._left_rotate(parent)
                #接下来对比旋转后的兄弟
                brother = parent.right

            #由于经过上面的处理，兄弟节点肯定为黑色,兄弟节点两个子节点都为黑色
            if (brother.left is self.null_leaf or brother.left.is_black()) and \
                (brother.right is self.null_leaf or brother.right.is_black()):
                brother.mark_as_red()
                current_node = current_node.parent
            else:
                if current_node == current_node.parent.left:
                    if not brother.right or brother.right.is_black():
                        brother.mark_as_red()
                        brother.left.mask_as_black()
                        self._right_rotate(brother)
                        brother = parent.right
                    brother.color = parent.color
                    parent.mask_as_black()
                    brother.right.mask_as_black()
                    self._left_rotate(parent)
                else:
                    if not brother.left or brother.left.is_black():
                        brother.mark_as_red()
                        brother.left.mask_as_black()
                        self._left_rotate(brother)
                        brother = parent.left
                    brother.color = parent.color
                    parent.mask_as_black()
                    brother.right.mask_as_black()
                    self._right_rotate(parent)
            current_node = self.root
            break
        node.mark_as_black()

    def _transplant(self,node_will_replace,node_replace):
        """
        用node_replace 结点代替node_will_replace
        :param tree 树的根节点
        :param node_will_replace 将被替换的节点
        :param node_replace 替换后的节点
        """
        if not node_will_replace.parent:
            self.root = node_replace
        # 将要被替换的节点是它父亲节点的左节点还是右节点，来决定node_replace的位置
        elif node_will_replace == node_will_replace.parent.left:
            node_will_replace.parent.left = node_replace
        elif node_will_replace == node_will_replace.parent.right:
            node_will_replace.parent.right = node_replace
        
        #父亲节点设置
        if node_replace:
            node_replace.parent = node_will_replace.parent


    def _left_rotate(self,node):
        if node is None:
            return
        parent = node.parent
        right = node.right

        node.right = right.left
        if node.right is not self.null_leaf:
            node.right.parent = node
        
        right.left = node
        node.parent = right

        right.parent = parent
        
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right

    def _right_rotate(self,node):

        parent = node.parent
        left = node.left

        node.left = left.right
        if node.left is not self.null_leaf:
            node.left.parent = node


        left.right = node
        node.parent = left

        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left
    
    def _parent(self,node):
        if node is None:
            return None
        else:
            return node.parent

    def _uncle(self,node):
        if node is None or self._parent(node) is None:
            return None
        else:
            return self._brother(self._parent(node))

    def _grandfather(self,node):
        if node is None or self._parent(node) is None:
            return None
        else:
            return self._parent(self._parent(node))

    def _brother(self,node):
        if node is None or node.parent is None:
            return None
        else:
            p = node.parent
            if node == p.left:
                return p.right
            else:
                return p.left

if __name__ == "__main__":
    red_black_tree = RedBlackTree()
    red_black_tree.insert(3)
    red_black_tree.insert(1)
    red_black_tree.insert(5)
    red_black_tree.insert(7)
    red_black_tree.insert(6)
    red_black_tree.insert(8)
    red_black_tree.insert(9)
    red_black_tree.insert(10)

    red_black_tree.delete(10)
    red_black_tree.delete(9)
    red_black_tree.delete(8)
    red_black_tree.delete(7)
    red_black_tree.delete(6)
    red_black_tree.delete(3)
    red_black_tree.delete(1)
    red_black_tree.delete(5)


                    
                    

