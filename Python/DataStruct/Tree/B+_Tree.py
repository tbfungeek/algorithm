import bisect
import math

"""
叶子结点
"""
class Leaf:

    def __init__(self, previous_leaf, next_leaf, parent, branching_factor=16):
        #前驱叶子
        self.previous = previous_leaf
        #后驱叶子
        self.next = next_leaf
        #父亲结点
        self.parent = parent
        #分子因子
        self.branching_factor = branching_factor
        #用于存储key的结点
        self.keys = []
        #用于存储值的结点
        self.children = [] 

    def set(self, key, value):
        #通过二分查找是否已经有待插入key的数据
        index = bisect.bisect_left(self.keys, key)
        #如果找到了就将该值更新
        if index < len(self.keys) and self.keys[index] == key:
            self.children[index] = value
        else:
        #如果没找到则在key value的最后插入数据
            self.keys.insert(index, key)
            self.children.insert(index, value)
            #如果数据尺寸到达分支因子，则说明分支已经满了，则开始分割结点
            if self.size() == self.branching_factor:
                #每个叶子分支8个结点
                self.split(math.ceil(self.branching_factor / 2))

    def get(self, key):
        index = self.keys.index(key)
        return self.children[index]

    def split(self, index):

        #新建一个叶子结点，它的前结点为当前结点，下个结点为self.next，将它挂在self.parent下面
        self.next = Leaf(self, self.next, self.parent, self.branching_factor)
        
        #从index之后的所有结点都存到self.next
        self.next.keys = self.keys[index:]
        self.next.children = self.children[index:]

        #从index之前的都放到当前结点
        self.keys = self.keys[:index]
        self.children = self.keys[:index]
        
        #如果当前结点为根结点，则新生成一个node结点作为它的父结点
        if self.is_root():
            #父结点包含next的左边界key以及self 和 self.next指针，TODO:B+树不是每个结点包含的keys和value是一对一的吗？
            parent = Node(None, None, [self.next.keys[0]], [self, self.next], branching_factor=self.branching_factor)
            #将新生成的结点作为next的父结点
            self.next.parent = parent
            #将新生成的结点作为当前结点的父结点
            self.parent = parent
        else:
            #如果当前结点不是根结点，说明已经存在父结点了，那么在父结点上添加索引
            self.parent.add_child(self.next.keys[0], self.next)
        return self.next

    def remove_item(self, key):
        del_index = self.keys.index(key)
        self.keys.pop(del_index)
        removed_item = self.children.pop(del_index)
        self.balance()
        return removed_item

    def balance(self):
        if not self.is_root() and self.size() < self.branching_factor // 2:
            # Borrow from siblings
            if self.previous is not None and self.previous.size() > self.branching_factor // 2:
                self.keys.insert(0, self.previous.keys.pop(-1))
                self.children.insert(0, self.previous.children.pop(-1))
                self.parent.change_key(self.keys[0], self.keys[0])
            elif self.next is not None and self.next.size() > self.branching_factor // 2: 
                self.keys.insert(-1, self.next.keys.pop(0))
                self.children.insert(-1, self.next.children.pop(0))
                self.next.parent.change_key(self.keys[0], self.next.keys[0])
            # Merge. Always merge left.
            elif self.previous is not None:
                del_key = self.previous.keys[-1]
                self.previous.keys.extend(self.keys)
                self.previous.children.extend(self.children)
                self.parent.remove_child(del_key)
            elif self.next is not None:
                del_key = self.keys[-1]
                self.keys.extend(self.next.keys)
                self.children.extend(self.next.children)
                self.parent.remove_child(del_key)

    def is_root(self):
        return self.parent is None

    def size(self):
        return len(self.children)


class Node:
    def __init__(self, previous_node, next_node, keys, children, parent=None, branching_factor=16):
        self.previous = previous_node
        self.next = next_node
        self.keys = keys # NOTE: must keep keys sorted
        self.children = children # NOTE: children must correspond to parents.
        self.parent = parent
        self.branching_factor = branching_factor
        for child in children:
            child.parent = self

    def set(self, key, value):
        for i, k in enumerate(self.keys):
            if key < k:
                self.children[i].set(key, value)
                return
        self.children[i + 1].set(key, value)


    def get(self, key):
        for i, k in enumerate(self.keys):
            if key < k:
                return self.children[i].get(key)
        return self.children[i + 1].get(key)


    def add_child(self, key, greater_child):
        #找到插入的位置
        index = bisect.bisect(self.keys, key)
        #将索引插入到对应的位置
        self.keys.insert(index, key)
        #将结点插入到对应的位置
        self.children.insert(index + 1, greater_child)
        #查看当前非叶子结点是否超过分支因子，如果超过则对齐进行拆分
        if len(self.keys) == self.branching_factor:
            self.split(self.branching_factor // 2)


    def change_key(self, old_key, new_key):
        """Replaces the first key that is greater or equal than
        old_key with new_key or modifies the parent's key so that new_key
        falls within the current node"""
        if new_key < self.keys[0]:
            self.parent.change_key(self.keys[0], new_key)
        for i, k in enumerate(self.keys):
            if k >= old_key:
                self.keys[i] = new_key

    def split(self, index):

        #新生成一个非叶子结点，前结点为当前结点，下一个结点为新生成的这个结点，key，children 为index + 1 之后的结点，和当前的结点公用一个parent
        self.next = Node(self, self.next, self.keys[index + 1:], self.children[index + 1:], self.parent)

        split_key = self.keys[index]

        #处理当前结点数据
        self.keys = self.keys[:index]
        self.children = self.children[:index + 1]

        #如果是叶子结点则，新生成一个父结点
        if self.is_root():
            self.parent = Node(None, None, [split_key], [self, self.next], branching_factor=self.branching_factor)
        else:
        #如果不是叶子结点则在原有的叶子结点上添加中间数据
            self.parent.add_child(split_key, self.next)

        return self.next

    def remove_item(self, key):
        """Removes item corresponding to key in the tree.
        """
        for i, k in enumerate(self.keys):
            if k >= key:
                self.children[i].remove_item(key)
                return
        return self.children[-1].remove_item(key)

    def remove_child(self, key):
        """Removes first key that is greater that or equal to
        key and the child to the right of that key.
        Returns the removed child.
        """
        removed_child = None
        for i, k in enumerate(self.keys):
            if k >= key:
                self.keys.pop(i)
                removed_child = self.children.pop(i + 1)
                if removed_child.previous is not None:
                    removed_child.previous.next = removed_child.next
                if removed_child.next is not None:
                    removed_child.next.previous = removed_child.previous
                break
        self.balance()
        return removed_child

    def balance(self):
        # Borrow from siblings if necessary
        if not self.is_root() and self.size() < self.branching_factor // 2:
            if self.previous is not None and self.previous.size() > self.branching_factor // 2:
                self.keys.insert(0, self.previous.keys.pop(-1))
                self.children.insert(0, self.previous.children.pop(-1))
                self.parent.change_key(self.keys[0], self.keys[0])
            elif self.next is not None and self.next.size() > self.branching_factor // 2: 
                self.keys.insert(-1, self.next.keys.pop(0))
                self.children.insert(-1, self.next.children.pop(0))
                self.next.parent.change_key(self.keys[0], self.next.keys[0])
            # Merge. Always merge left.
            elif self.previous is not None:
                del_key = self.previous.keys[-1]
                self.previous.keys.extend(self.keys)
                self.previous.children.extend(self.children)
                self.parent.remove_child(del_key)
            elif self.next is not None:
                del_key = self.keys[-1]
                self.keys.extend(self.next.keys)
                self.children.extend(self.next.children)
                self.parent.remove_child(del_key)
        # Make child the root only 1 child
        if self.is_root() and len(self.children) == 1:
            # TODO: make child root of greater tree
            self.children[0].parent = None

    def is_root(self):
        return self.parent is None

    def size(self):
        return len(self.children)

class BPlusTree:

    def __init__(self, branching_factor=16):
        self.branching_factor = branching_factor

        #生成一个用于遍历所有叶子结点的索引结点
        self.leaves = Leaf(None, None, None, branching_factor) 
        #root指向索引结点
        self.root = self.leaves

    def set(self, key, value):
        #将key value 添加到对应结点
        self.root.set(key, value)
        if self.root.parent is not None:
            self.root = self.root.parent

    def get(self, key):
        return self.root.get(key)

    def __getitem__(self, key):
        return self.get(key)

    def remove_item(self, key):
        self.root.remove_item(key)
        if type(self.root) is Node and len(self.root.children) == 1:
            self.root = self.root.children[0]

    def __delitem__(self, key):
        return self.remove_item(key)


    def __setitem__(self, key, value):
        return self.set(key, value)

    def size(self):
        result = 0
        leaf = self.leaves
        while leaf is not None:
            result += leaf.size()
            leaf = leaf.next
        return result

    def split(self, key):
        tree = BPlusTree()
        tree.root = Node(None, None, [], [], self.branching_factor)

        current_node = self.root
        new_node = tree.root
        while type(current_node) is Node or type(current_node) is Leaf:
            child_type = type(current_node.children[0])
            split_index = bisect.bisect_left(current_node.keys, key)
            new_node.keys = current_node.keys[:split_index]
            new_node.children = current_node.children[:split_index]
            current_node.keys = current_node.keys[split_index:]
            current_node.children = current_node.children[split_index:]
            if len(current_node.children) == 0:
                break
            # Add new ambiguous node on the split and fix pointers
            if child_type is Node:
                new_node.children.append(Node(new_node.children[-1], None, [], [],
                                              parent=new_node,
                                              branching_factor=new_node.branching_factor))
                new_node.children[-2].next = new_node.children[-1]
                current_node.children[0].previous = None
            elif child_type is Leaf:
                new_node.children.append(Leaf(new_node.children[-1], None, new_node,
                                              branching_factor=new_node.branching_factor))
                new_node.children[-2].next = new_node.children[-1]
                current_node.children[0].previous = None
            # Balance trees
            new_node.balance()
            current_node.balance()
            current_node = current_node.children[0]
            new_node = new_node.children[-1]

        return tree


if __name__ == "__main__":
    bp_tree = BPlusTree(16)

    for item in range(0,18):
        bp_tree.set(item,"value"+str(item))
