#-*-coding:utf-8-*-
#!/usr/bin/env python3

class BNode(object):
    
    def __init__(self,data, prev = None, next = None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    @property
    def data(self):
        return self.__data 

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self,prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self,next):
        self.__next = next

    def __str__(self):
        return str(self.__data)

class BidirectionLinkList(object):

    def __init__(self):
        self.__head = self.create_node(None)
        self.__count = 0
    
    def create_node(self, data):
        node = BNode(data)
        #create node which prev && next point to self
        node.prev = node
        node.next = node
        return node

    def isEmpty(self):
        if self.__head.prev == self.__head and self.__head.next == self.__head:
            return True
        return False

    def size(self):
        return self.__count

    def get(self,index):
        if index < 0 or index >= self.__count:
            return None
        if self.isEmpty(): 
            return None
        if index <= self.__count / 2:
            current_node = self.__head.next
            current_index = 0
            while current_node != self.__head:
                if current_index == index:
                    return current_node
                current_index += 1
                current_node = current_node.next
        else:
            current_node = self.__head.prev
            current_index = 0 
            while current_node != self.__head:
                if current_index == self.__count - 1 - index:
                    return current_node
                current_index += 1
                current_node = current_node.prev

    def first(self):
        if self.isEmpty():
            return None
        return self.__head.next

    def last(self):
        if self.isEmpty():
            return None
        return self.__head.prev

    def insert_value_to_head(self,value):
        if value is None:
            return
        node = BNode(value)
        node.next = self.__head.next
        self.__head.next.prev  = node
        node.prev = self.__head
        self.__head.next = node
        self.__count += 1

    def insert_value_before(self,value,new_value):
        if value is None or new_value is None:
            return
        if self.isEmpty():
            return
        node = BNode(new_value)
        current_node = self.__head.next
        while current_node != self.__head:
            if current_node.data == value:
                node.next = current_node
                current_node.prev.next = node
                node.prev = current_node.prev
                current_node.prev = node
                self.__count += 1
                return
            current_node = current_node.next

    def insert_value_after(self,value,new_value):
        if value is None or new_value is None:
            return
        if self.isEmpty():
            return
        node = BNode(new_value)
        current_node = self.__head.next
        while current_node != self.__head:
            if current_node.data == value:
                node.next = current_node.next
                current_node.next.prev = node
                current_node.next = node
                node.prev = current_node
                return
            current_node = current_node.next

    def insert_value_to_tail(self,value):
        if value is None:
            return
        if self.isEmpty():
            self.insert_value_to_head(value)
            return
        node = BNode(value)
        tail_node = self.__head.prev
        node.next = tail_node.next
        tail_node.next.prev = node
        tail_node.next = node
        node.prev = tail_node

    def delete_head_node(self):
        pass

    def delete_value_before(self,value):
        pass

    def delete_value_after(self,value):
        pass

    def delete_tail_value(self):
        pass

    def __str__(self):
        if self.isEmpty():
            return None
        value = []
        for item in self:
            value.append(str(item.data))
        return " ==> ".join(value)

    def __iter__(self):
        if self.isEmpty():
            return None
        current_node = self.__head.next
        while current_node != self.__head:
            yield current_node
            current_node = current_node.next

if __name__ == "__main__":

    b_link_list = BidirectionLinkList()
    b_link_list.insert_value_to_head(1)
    b_link_list.insert_value_to_head(2)
    b_link_list.insert_value_to_head(3)
    b_link_list.insert_value_to_head(4)
    b_link_list.insert_value_to_head(5)
    print(b_link_list.get(5))
    print(b_link_list.first())
    print(b_link_list.last())
    print(b_link_list)
    b_link_list.insert_value_before(1,111)
    print(b_link_list)
    b_link_list.insert_value_before(5,111)
    print(b_link_list)
    b_link_list.insert_value_before(3,111)
    print(b_link_list)
    b_link_list.insert_value_after(111,222)
    print(b_link_list)
    b_link_list.insert_value_after(1,222)
    print(b_link_list)
    b_link_list.insert_value_to_tail(888)
    print(b_link_list)


