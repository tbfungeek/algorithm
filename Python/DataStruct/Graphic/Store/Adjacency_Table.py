class Vertex(object):

    def __init__(self,value):
        self.__value = value
        self.__connected_vertexs = {}

    @property
    def connected_vertexs(self):
        return self.__connected_vertexs

    @connected_vertexs.setter
    def connected_vertexs(self, connected_vertexs):
        self.__connected_vertexs = connected_vertexs;

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def add_connected_vertex(self, vertex, weight = 0):
        if vertex == self or vertex is None:
            return
        self.connected_vertexs[vertex] = weight
    
    def weight_to_vertex(self, vertex):
        return self.connected_vertexs[vertex]

    def __str__(self):
        return str(self.value) + "  connectedTo " + str([x.value for x in self.connected_vertexs])
        

class Adjacency_Table(object):

    def __init__(self):
        self.__vertexs = {}
        self.__count = 0

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self,count):
        self.__count = count

    @property
    def vertexs(self):
        return self.__vertexs

    @vertexs.setter
    def vertexs(self, vertex):
        self.__vertexs = vertex

    def __add_vertex(self,value):
        if value in self.vertexs:
            return
        self.count += 1
        vertex = Vertex(value)
        self.vertexs[value] = vertex

    def __get_vertex(self,value):
        if value in self.vertexs:
            return self.vertexs[value]
        else:
            return None
    
    def contain(self,value):
        return value in self.vertexs
    
    def add_Edge(self,from_vertex,to_vertex,weight):
        self.__add_vertex(from_vertex)
        self.__add_vertex(to_vertex)
        self.__get_vertex(from_vertex).add_connected_vertex(self.__get_vertex(to_vertex),weight)

    def is_vertex_connected(self,from_vertex,to_vertex):
        return self.__get_vertex(to_vertex) in  self.__get_vertex(from_vertex).connected_vertexs

    def __iter__(self):
        return iter(self.vertexs.values())

if __name__ == '__main__':
    graphic = Adjacency_Table()
    graphic.add_Edge(0,1,5)
    graphic.add_Edge(0,5,2)
    graphic.add_Edge(1,2,4)
    graphic.add_Edge(2,3,9)
    graphic.add_Edge(3,4,7)
    graphic.add_Edge(3,5,3)
    graphic.add_Edge(4,0,1)
    graphic.add_Edge(5,4,8)
    graphic.add_Edge(5,2,1)

    for vertex in graphic:
        print(vertex)

    print(graphic.is_vertex_connected(0,4))
    print(graphic.is_vertex_connected(1,2))

    

