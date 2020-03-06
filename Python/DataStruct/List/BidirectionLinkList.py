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
        pass

    def first(self):
        pass

    def last(self):
        pass

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
        pass

    def insert_value_after(self,value,new_value):
        pass

    def insert_value_to_tail(self,value):
        pass

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

    print(b_link_list)
