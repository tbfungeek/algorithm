class Adjacency_Matrix(object):

    def __init__(self,node_count = 0,is_directed = False):
        self.__node_count   = node_count
        self.__is_directed  = is_directed
        self.__G            = [[0] * node_count for _ in range(node_count)]
        self.__edges        = []

    @property
    def node_count(self):
        return self.__node_count
    
    @node_count.setter
    def node_count(self,node_count):
        self.__node_count = node_count

    @property
    def edges(self):
        return self.__edges
    
    @edges.setter
    def edges(self,edges):
        self.__edges = edges

    @property
    def is_directed(self):
        return self.__is_directed

    @is_directed.setter
    def is_directed(self,is_directed):
        self.__is_directed = is_directed

    @property
    def G(self):
        return self.__G

    @G.setter
    def G(self,G):
        self.__G = G
    
    def add_edge(self,edge_node1,edge_node2,weight = 1):
        if edge_node1 >= self.node_count or edge_node2 >= self.node_count:
            return
        
        self.G[edge_node1][edge_node2] = weight
        if not self.is_directed:
            self.G[edge_node2][edge_node1] = weight
        else:
            self.G[edge_node2][edge_node1] = 0

        self.edges.append((edge_node1,edge_node2))  

    def is_adjust(self,node1,node2):
        if node1 >= self.node_count or node2 >= self.node_count:
            return False
        
        if not self.is_directed:
            return (self.G[node1][node2] == self.G[node2][node1]) and (self.G[node2][node1] != 0)
        else:
            return (self.G[node1][node2] != 0) and (self.G[node2][node1] == 0)
        
    def show_graphic(self):
        print(self.G)

if __name__ == '__main__':
    matrix = Adjacency_Matrix(5)
    matrix.add_edge(0,1)
    matrix.add_edge(1,2)
    matrix.add_edge(1,3)
    matrix.add_edge(1,4)
    matrix.add_edge(3,4)
    matrix.add_edge(3,2)

    matrix.show_graphic()

    print(matrix.is_adjust(3,1))
    print(matrix.edges)


    
    