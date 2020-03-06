class Node(object):

    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next

    def __str__(self):
        return str(self.__data)


class HashTable(object):

    def __init__(self, table_size):
        self.__table_size = table_size
        self.__table = [None] *table_size

    def insert(self, data):
        if data is None:
            return
        hash_index = data % self.__table_size
        node = Node(data)
        if self.__table[hash_index] is None:
            self.__table[hash_index] = node
        else:
            current_node = self.__table[hash_index]
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def delete(self,data):
        if data is None:
            return
        hash_index = data % self.__table_size
        if self.__table[hash_index] is None:
            return
        current_node = self.__table[hash_index]
        prev_node = current_node
        while current_node != None:
            if current_node.data == data:
                if current_node == self.__table[hash_index]:
                    self.__table[hash_index] = None
                    return
                if current_node.next == None:
                    prev_node.next = None
                    return
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next

    def get(self,data):
        if data is None:
            return
        hash_index = data % self.__table_size
        if self.__table[hash_index] is None:
            return
        current_node = self.__table[hash_index]
        while current_node != None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

    def __str__(self):

        value = []
        for index_item in self.__table:
            if index_item != None:
                value.append(str(index_item))
            else:
                value.append("None")

        index_str = "index :" + " ===> ".join(value)

        index = 0
        for index_item in self.__table:
            current_node = index_item;
            temp = []
            while current_node != None:
                temp.append(str(current_node.data))
                current_node = current_node.next
            index += 1
            s = "      ["+str(index)+"]" + "---->".join(temp)
            index_str += s
        return index_str
            
if __name__ == '__main__':

    hash_table = HashTable(10)
    
    for value in range(0,15):
        hash_table.insert(value)

    print(hash_table)

    print(hash_table.get(10))

    hash_table.delete(13)
    hash_table.delete(3)

    print(hash_table.get(13))
    print(hash_table.get(3))

    print(hash_table)

    