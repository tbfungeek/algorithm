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
        pass

    def delete(self,data):
        pass

    def get(self,data):
        pass

    def __str__(self):

        value = []
        for index_item in self.__table:
            if index_item != None:
                value.append(str(index_item))
            else:
                value.append("None")

        return " ===> ".join(value)

if __name__ == '__main__':

    hash_table = HashTable(10)

    print(hash_table)
    