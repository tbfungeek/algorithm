class BTreeNode(object):
    
    def __init__(self,capacity = 0, is_leaf = True):
        self.__capacity    = capacity
        self.__is_leaf     = is_leaf
        self.__index       = 0
        self.__keys        = [0] * self.__capacity
        self.__children    = [None] * (self.__capacity + 1)

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def is_leaf(self):
        return self.__is_leaf

    @is_leaf.setter
    def is_leaf(self, is_leaf):
        self.__is_leaf = is_leaf

    @property
    def keys(self):
        return self.__keys
    
    @keys.setter
    def keys(self,keys):
        self.__keys = keys
    
    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self,index):
        self.__index = index

    def is_full_node(self):
        return self.index == self.__capacity

    @staticmethod
    def create_node(key_max,is_leaf = False):
        return BTreeNode(key_max, is_leaf)

class BTree(object):

    def __init__(self, node_min_count = 3):

        """
        可以参照2-3树的定义理解：
        结点要么为空要么是如下两种结点
        2节点: 该节点保存1个key，以及两个指向左右节点的节点
        3节点: 该节点保存2个key，以及三个指向左右节点的节点
        """

        self.__root: BTreeNode = None
        # B 树的最小度数
        self.M = node_min_count
        # 结点包含的最多关键字个数
        self.KEY_MAX = 2 * self.M - 1
        # 结点包含的最少关键字个数
        self.KEY_MIN = self.M - 1
        # 子结点的最大个数
        self.CHILD_MAX = self.KEY_MAX + 1
        # 子结点的最小个数
        self.CHILD_MIN = self.KEY_MIN + 1

        print("")

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def __generate_node(self,is_leaf = True):
        return BTreeNode.create_node(self.KEY_MAX,is_leaf)

    def insert(self, key):

        #已经存在的情况下就不执行插入操作了
        if self.contain(key):
            return
        else:
            #如果是空树的情况下进行插入，新生成一个结点作为根结点
            if self.root is None:
                node = self.__generate_node()
                self.root = node
            
            #如果根结点满的情况，先扩展结点
            elif self.root.is_full_node():
                new_node = self.__generate_node(False)
                #将根结点作为新结点的第一个子结点
                new_node.children[0] = self.root
                #__split_node 这里将根结点拆分出一个右结点，作为new_node的右边结点
                self.__split_node(new_node,0,self.root)
                #新的结点作为新的根结点
                self.root = new_node
            
            #统一执行插入操作
            self.__insert(self.root,key)

    def contain(self, key):
        return self.__search(self.root,key)

    def __search(self,node:BTreeNode,key):
        #如果根结点是空的则直接返回
        if node is None:
            return False
        else:
            i = 0
            #遍历索引结点
            while i < node.index and key > node.keys[i]:
                i += 1

            #在当前结点找到
            if i < node.index and key == node.keys[i]:
                return True
            else:
                #如果没找到，并且已经是叶子结点了，没法继续查找所以直接返回False结果
                if node.is_leaf:
                    return False
                else:
                    #如果不是叶子结点说明还可以继续往下找，则递归寻找
                    return self.__search(node.children[i],key)

    def __split_node(self,result_node,splite_from,orginal_node):
        
        #新生成一个和orginal_node类型一样的右结点
        right_node = self.__generate_node(orginal_node.is_leaf)
        right_node.index = self.KEY_MIN

        #将原始结点超出的部分放置到右结点上
        for i in range(self.KEY_MIN):
            right_node.keys[i] = orginal_node.keys[i + self.CHILD_MIN]

        #如果待分裂的结点不是叶子结点那么还需要处理子结点的拷贝
        if not orginal_node.is_leaf:
            for i in range(self.CHILD_MIN):
                right_node.children[i] = orginal_node.children[i + self.CHILD_MIN]

        #将index设置为满的状态
        orginal_node.index = self.KEY_MIN

        #将result结点从splite_from开始向后移动结点
        for i in range(splite_from, result_node.index):
            j = result_node.index + splite_from - i
            result_node.children[j+1] = result_node.children[j]
            result_node.keys[j] = result_node.keys[j-1]
        

        #将right_node 和 orginal_node 作为 result_node 的子结点
        result_node.children[splite_from + 1] = right_node
        result_node.keys[splite_from] = orginal_node.keys[self.KEY_MIN]
        result_node.index += 1

    def __insert(self, node:BTreeNode, key):
        # 获取结点内关键字个数
        i = node.index
        # 如果node是叶子结点
        if node.is_leaf == True:
            # 从后往前 查找关键字的插入位置
            while i > 0 and key < node.keys[i - 1]:
                # 向后移位
                node.keys[i] = node.keys[i - 1]
                i -= 1
            # 插入关键字的值
            node.keys[i] = key
            # 更新结点关键字的个数
            node.index += 1
        # node是非叶子结点
        else:
            # 从后往前 查找关键字的插入的子树
            while i > 0 and key < node.keys[i - 1]:
                i -= 1
            # 目标子树结点指针
            target_child = node.children[i]
            if target_child is None:
                return

            # 子树结点已经满了
            if target_child.is_full_node():
                # 分裂子树结点
                self.__split_node(node, i, target_child)
                # 确定目标子树
                if key > node.keys[i]:
                    target_child = node.children[i + 1]
            # 插入关键字到目标子树结点
            self.__insert(target_child, key)

    def delete(self,key):

        #关键字不存在的情况下直接返回
        if not self.contain(key):
            return

        #只有一个结点的情况下
        if self.root.index == 1:
            #根结点是叶子结点
            if self.root.is_leaf:
                self.destroy()
            else:
                #根结点下面还有下一层次，需要处理下个层次的关系
                left_child = self.root.children[0]
                right_child = self.root.children[1]
                if left_child.index == self.KEY_MIN and right_child.index == self.KEY_MIN:
                    self.__merge_child(self.root,0)
                    self.__delete_node(self.root)
                    self.root = left_child
        
        self.__recursive_remove(self.root,key)

    def __merge_child(self,node:BTreeNode,index):
        
        child1 = node.children[index]
        child2 = node.children[index + 1]

        #将index + 1 结点合并到 index 结点
        child1.index = self.KEY_MAX
        #将父结点到index值下移到child1
        child1.keys[self.KEY_MIN] = node.keys[index]

        #将child2 key添加到上面的结点之后
        for i in range(self.KEY_MIN):
            child1.keys[self.KEY_MIN + i + 1] = child2.keys[i]
        #拷贝子结点
        if not child1.is_leaf:
            for i in range(self.CHILD_MIN):
                child1.children[i + self.CHILD_MIN] = child2.children[i]

        #删除child在父结点的数据
        node.index -= 1
        for i in range(index,node.index):
            node.keys[i] = node.keys[i+1]
            node.children[i+1]= node.children[i + 2]
        
        #删除child2 结点
        self.__delete_node(child2)
        

    def __delete_node(self,node:BTreeNode):
        if node is not None:
            node = None

    def __recursive_remove(self, node:BTreeNode, key):
        
        #在node层查找
        i = 0
        while i < node.index and key > node.keys[i]:
            i += 1
        
        if i < node.index and key == node.keys[i]:
            #在node层找到了
            if node.is_leaf:
                #node是叶子结点，从node中删除
                for j in range(i, node.index):
                    node.keys[j] = node.keys[j + 1]
                return 
                
            else:
                #node是内结点
                # 结点node中位于key之前的结点
                child_prev = node.children[i]
                # 结点node中位于key之后的结点
                child_next = node.children[i + 1]
                if child_prev.index >= self.CHILD_MIN:
                    # 获取key的前驱关键字
                    prev_key = self.predecessor(child_prev)
                    self.__recursive_remove(child_prev,prev_key)
                    # 替换成key的前驱关键字
                    node.keys[i] = prev_key
                    return
                # 结点pChildNext中至少包含CHILD_MIN个关键字
                elif child_next.index >= self.CHILD_MIN:
                    # 获取key的后继关键字
                    next_key = self.successor(child_next)
                    self.__recursive_remove(child_next,next_key)
                    # 替换成key的后继关键字
                    node.keys[i] = next_key
                    return
                # 结点pChildPrev和pChildNext中都只包含CHILD_MIN-1个关键字
                else:
                    self.__merge_child(node,i)
                    self.__recursive_remove(child_prev,key)
        else:
            #在node层没找到
            child = node.children[i]
            if child.index == self.KEY_MAX:
                # 左兄弟结点
                left = None
                # 右兄弟结点
                right = None
                # 左兄弟结点
                if i > 0:
                    left = node.children[i - 1]
                # 右兄弟结点
                if i < node.index:
                    right = node.children[i + 1]
                j = 0
                if left is not None and left.index >= self.CHILD_MIN:
                    # 父结点中i-1的关键字下移至pChildNode中
                    for j in range(child.index):
                        k = child.index - j
                        child.keys[k] = child.keys[k - 1]
                    child.keys[0] = node.keys[i - 1]
                    if not left.is_leaf:
                        for j in range(child.index + 1):
                            k = child.index + 1 - j
                            child.children[k] = child.children[k - 1]
                        child.children[0] = left.children[left.index]
                    child.index += 1
                    node.keys[i] = left.keys[left.index - 1]
                    left.index -= 1
                # 右兄弟结点至少有CHILD_MIN个关键字
                elif right is not None and right.index >= self.CHILD_MIN:
                    # 父结点中的i的关键字下移到child结点
                    child.keys[child.index] = node.keys[i]
                    child.index += 1
                    #right结点中最小的关键字上升到node中
                    node.keys[i] = right.keys[0]
                    right.index -= 1
                    for j in range(right.index):
                        right.keys[j] = right.keys[j + 1]
                    if not right.is_leaf:
                        child.children[child.index] = right.children[0]
                        for j in range(right.index):
                            right.children[j] = right.children[j + 1]
                # 左右兄弟结点都只包含CHILD_MIN-1个结点
                elif left is not None:
                    self.__merge_child(node, i - 1)
                    child = left
                # 与右兄弟合并
                elif right is not None:
                    self.__merge_child(node, i)
            self.__recursive_remove(child,key)

    def destroy(self):
        self.__recursive_clear(self.root)
        self.root = None

    def __recursive_clear(self, node:BTreeNode):

        #如果结点是空的则不做任何处理
        if node is None:
            return 
        #如果结点不是叶子结点
        if not node.is_leaf:
            #对每个子结点进行遍历删除
            for i in range(node.index):
                self.__recursive_clear(node.children[i])
        #删除某个结点
        self.__delete_node(node)
    
    def predecessor(self, node: BTreeNode):
        while not node.is_leaf:
            node = node.children[node.index]
        return node.keys[node.index - 1]

    def successor(self, node: BTreeNode):
        while not node.is_leaf:
            node = node.children[0]
        return node.keys[0]

if __name__ == "__main__":
    tree = BTree(3)
    tree.insert(11)
    tree.insert(3)
    tree.insert(1)
    tree.insert(4)
    tree.insert(33)
    tree.insert(13)
    tree.insert(63)
    tree.insert(43)
    tree.insert(2)
    tree.insert(123)
    tree.insert(55)
    tree.destroy()
    tree = BTree(2)
    tree.insert(11)
    tree.insert(3)
    tree.insert(1)
    tree.insert(4)
    tree.insert(33)
    tree.insert(13)
    tree.insert(63)
    tree.insert(43)
    tree.insert(2)
    tree.delete(1)
    tree.delete(2)
    tree.delete(3)
    tree.destroy()




    




        
        

    