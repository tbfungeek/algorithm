#-*-coding:utf-8-*-
#!/usr/bin/env python3

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    

class SimpleLinkList(object):

    def __init__(self):
        #int with None head node
        self._head = None

    def insert_value_to_head(self,value):
        node = Node(value)
        # point the node next to current head
        node.next = self._head   
        # use node as head node 
        self._head = node

    def insert_value_before(self,value,new_value):
        if value == None or self._head == None or new_value == None:
            return
        #create a new node
        node = Node(new_value)
        #if find in head node insert to head 
        if self._head.data == value:
            self.insert_value_to_head(new_value)
        else:
            #begin to find
            current_node = self._head
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
        current_node = self._head
        while current_node != None:
            if current_node.data == value:
                node.next = current_node.next
                current_node.next = node
                return
            current_node = current_node.next 
        
    
    def fine_value(self,value):
        if not value or not self._head:
            return None
        current_node = self._head
        while current_node != None:
            if current_node.data == value:
                return current_node
            current_node = current_node.next
        
    def delete_value(self,value):
        if not value or not self._head:
            return

        if self._head.data == value:
            self._head = self._head.next
            return

        current_node = self._head
        while current_node.next != None:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


    #when use for in xxx this function will call
    def __iter__(self):
        if self._head == None:
            yield None
        current_node = self._head
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

