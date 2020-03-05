#-*-coding:utf-8-*-
#/usr/bin/env python3

class Node(object):

    def __init__(self,data,next = None):
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

class CircleLinkList(object):

    def __init__(self):
        self.__head = None
    
    @property
    def head(self):
        return self.__head

    def insert_value_to_head(self,value):
        if value is None:
            return
        node = Node(value)
        #in case of insert into empty list
        if self.__head == None:
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            current_node = self.head
            while current_node.next is not self.__head:
                current_node = current_node.next
            current_node.next = node
            self.__head = node

    def insert_value_before(self, value, new_value):
        if value is None or new_value is None:
            return
        
        if self.__head is None or self.__head.data == value:
            self.insert_value_to_head(new_value)
        else:
            current_node = self.__head.next
            prev_node = current_node
            node = Node(new_value)
            while current_node != self.__head:
                if current_node.data == value:
                    node.next = current_node
                    prev_node.next = node
                    return 
                prev_node = current_node
                current_node = current_node.next

    def insert_value_after(self, value, new_value):
        if value is None or new_value is None:
            return
        node = Node(new_value)
        if self.__head.data == value:
            node.next = self.__head.next
            self.__head.next = node
        else:
            current_node = self.__head.next
            while current_node != self.__head:
                if current_node.data == value:
                    node.next = current_node.next
                    current_node.next = node
                    return
                current_node = current_node.next

    def find_value(self,value):
        
        if value is None:
            return None
        if self.__head is None:
            return None
        if self.__head.data == value:
            return self.__head
        
        current_node = self.__head.next
        while current_node.next != self.__head:
            if current_node.data == value:
                return current_node
            current_node = current_node.next

    def delete_value(self, value):
        if value is None:
            return
        if self.__head.data == value:
            current_node = self.__head.next
            while current_node.next != self.__head:
                current_node = current_node.next
            current_node.next = self.__head.next
            self.__head = self.__head.next
        else:
            current_node = self.__head.next
            prev_node = current_node
            while current_node != self.__head:
                if current_node.data == value:
                    #in case of tail
                    if current_node.next == self.__head:
                        prev_node.next = self.__head
                    else:
                        prev_node.next = current_node.next
                prev_node = current_node
                current_node = current_node.next



    def __iter__(self):

        if self.__head is None:
            return None

        current_node = self.__head
        yield current_node
        current_node = current_node.next
        while current_node != self.__head:
            yield current_node
            current_node = current_node.next

    def __str__(self):

        if self.__head is None:
            return None

        value = []
        for item in self:
            value.append(str(item.data))

        return " ==> ".join(value)


if __name__ == "__main__":

    circleLinkList = CircleLinkList()
    circleLinkList.insert_value_to_head(4)
    circleLinkList.insert_value_to_head(2)
    circleLinkList.insert_value_to_head(3)
    circleLinkList.insert_value_before(3,111)
    circleLinkList.insert_value_before(4,222)
    circleLinkList.insert_value_after(111,888)
    circleLinkList.insert_value_after(4,8188)
    print(circleLinkList)

    print(circleLinkList.find_value(222))
    print(circleLinkList.find_value(111))
    print(circleLinkList.find_value(888))
    print(circleLinkList.find_value(818))
    circleLinkList.delete_value(111)
    print(circleLinkList)
    circleLinkList.delete_value(8188)
    print(circleLinkList)
    circleLinkList.delete_value(2)
    print(circleLinkList)