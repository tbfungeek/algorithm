

"""
结点基类
"""
class BaseNode(object):

    def __init__(self):
        self.__weight = 0
    
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,weight):
        self.__weight = weight
        
    def is_leaf(self):
        raise NotImplementedError("is_leaf should be implement in sub object")


"""
叶子结点，包含待编码的值，以及出现的频率
"""
class Leaf(BaseNode):

    def __init__(self,value = None, freq = 0):
        self.__value = value
        self.weight = freq
    
    def is_leaf(self):
        return True
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        self.__value = value

"""
中间结点 包含它的左右分支
"""
class Node(BaseNode):

    def __init__(self,left:BaseNode = None,right:BaseNode = None):
        
        self.__left = left
        self.__right = right

    def is_leaf(self):
        return False

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
    def weight(self):
        #权重为左右结点的权重和
        return self.left.weight + self.right.weight

class HuffmanTree(object):

    def __init__(self,flag, value = None, freq = 0, left = None, right = None):
        if flag == 0:
            self.__root = Leaf(value,freq)
        else:
            self.__root = Node(left.root,right.root)
    
    @property
    def root(self):
        return self.__root
    
    def weight(self):
        return self.root.weight

    def __encode(self,root:BaseNode,code,freq):
        if root.is_leaf():
            freq[root.value] = code
            return None
        else:
            self.__encode(root.left, code + "0",freq)
            self.__encode(root.right, code + "1",freq)

    def haffman_encode(self):
        result = {}
        self.__encode(self.root,"",result)
        return result

def buildHuffmanTree(tree_list):

    while len(tree_list) > 1:

        tree_list.sort(key=lambda x:x.root.weight)

        left = tree_list[0]
        right = tree_list[1]

        sub_tree = HuffmanTree(1,0,0,left,right)

        tree_list = tree_list[2:]

        tree_list.append(sub_tree)
    
    return tree_list[0]


if __name__ == "__main__":
    
    node_a = HuffmanTree(0,'A',5)
    node_b = HuffmanTree(0,'B',7)
    node_c = HuffmanTree(0,'C',2)
    node_d = HuffmanTree(0,'D',13)

    tree_list = [node_a,node_b,node_c,node_d]

    huffman_tree = buildHuffmanTree(tree_list)

    print(huffman_tree.haffman_encode())



        








    

    