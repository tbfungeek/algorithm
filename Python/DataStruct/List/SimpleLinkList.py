#-*-coding:utf-8-*-
#!/usr/bin/env python3

class Node(object):
    """链表节点对象"""

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
    

class SimpleLinkList(object):
    """单链表对象"""

    def __init__(self):
        #int with None head node
        self.__head = None

    def insert_value_to_head(self,value):
        if not value:
            return
        node = Node(value)
        # point the node next to current head
        node.next = self.__head   
        # use node as head node 
        self.__head = node

    def insert_value_before(self,value,new_value):
        if value == None or self.__head == None or new_value == None:
            return
        #create a new node
        node = Node(new_value)
        #if find in head node insert to head 
        if self.__head.data == value:
            self.insert_value_to_head(new_value)
        else:
            #begin to find
            current_node = self.__head
            #find while not reach to list tail
            while current_node.next != None:
                #find the node before 
                if current_node.next.data == value:
                    #insert after the node before
                    node.next = current_node.next
                    current_node.next = node
                    return
                current_node = current_node.next

    def insert_value_after(self,value,new_value):
        if not value or not new_value:
            return
        node = Node(new_value)
        current_node = self.__head
        while current_node != None:
            if current_node.data == value:
                node.next = current_node.next
                current_node.next = node
                return
            current_node = current_node.next 
        
    
    def fine_value(self,value):
        if not value or not self.__head:
            return None
        current_node = self.__head
        while current_node != None:
            if current_node.data == value:
                return current_node
            current_node = current_node.next
        
    def delete_value(self,value):
        if not value or not self.__head:
            return

        if self.__head.data == value:
            self.__head = self.__head.next
            return

        current_node = self.__head
        while current_node.next != None:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


    #when use for in xxx this function will call
    def __iter__(self):
        if self.__head == None:
            yield None
        current_node = self.__head
        while current_node:
            yield current_node
            current_node = current_node.next

    #when printf() is call this function will call
    def __str__(self):
        elements = []
        for node in simpleLinkList:
            if node == None:
                continue
            elements.append(str(node.data))
        return " ===> ".join(elements)

if __name__ == "__main__":

    simpleLinkList = SimpleLinkList()
    simpleLinkList.insert_value_to_head(45)
    simpleLinkList.insert_value_to_head(4)
    simpleLinkList.insert_value_to_head(5)
    simpleLinkList.insert_value_to_head(6)
    simpleLinkList.insert_value_to_head(9)
    print(simpleLinkList)
    simpleLinkList.insert_value_before(4,100)
    simpleLinkList.insert_value_before(9,100)
    print(simpleLinkList)
    simpleLinkList.insert_value_after(100,24)
    simpleLinkList.insert_value_after(45,67)
    print(simpleLinkList)
    print(simpleLinkList.fine_value(100));
    print(simpleLinkList.fine_value(67));
    simpleLinkList.delete_value(100)
    print(simpleLinkList)
    simpleLinkList.delete_value(67)
    print(simpleLinkList)

    simpleLinkList.delete_value(6)
    print(simpleLinkList)

