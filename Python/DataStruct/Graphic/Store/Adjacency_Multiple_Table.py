class Node(object):
    def __init__(self,value,first_edge):
        self.__value = value
        self.__first_edge = first_edge
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        self.__value = value
    
    @property
    def first_edge(self):
        return self.__first_edge
    
    @first_edge.setter
    def first_edge(self,first_edge):
        self.__first_edge = first_edge

class Edge(object):

    def __init__(self,ivex,ilink,jvex,jlink,info,mark):
        self.__ivex = ivex
        self.__jvex = jvex
        self.__info = info
        self.__ilink = ilink
        self.__jlink = jlink
        self.__mark = mark

    @property
    def ivex(self):
        return self.__ivex
    
    @ivex.setter
    def ivex(self, ivex):
        self.__ivex = ivex

    @property
    def jvex(self):
        return self.__jvex

    @jvex.setter
    def jvex(self,jvex):
        self.__jvex = jvex

    @property
    def ilink(self):
        return self.__ilink

    @ilink.setter
    def ilink(self, ilink):
        self.__ilink = ilink

    @property
    def jlink(self):
        return self.__jlink
    
    @jlink.setter
    def jlink(self, jlink):
        self.__jlink = jlink

    @property
    def info(self):
        return self.__info
    
    @info.setter
    def info(self, info):
        self.__info = info

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self,mark):
        self.__mark = mark

class Adjacency_Multiple_Table(object):
    
    def __init__(self):
        self.__nodes = []

    def add_node(self,value):
        node = Node(value,None)
        self.__nodes.append(node)

    def add_edge(self,ivex,jvex,info):
        node_len = len(self.__nodes)
        if ivex >= node_len or jvex >= node_len:
            return
        edge = Edge(ivex,None,jvex,None,info,False)

        #起点结点
        in_node:Node = self.__nodes[ivex]

        if in_node.first_edge == None:
            in_node.first_edge = edge
        else:
            in_edge = in_node.first_edge 
            while in_edge.ilink != None and in_edge.jvex != jvex:
                in_edge = in_edge.ilink
            
            if in_edge.ilink == None:
                #不存在就添加到末尾
                in_edge.ilink = edge
            else:
                #已经存在了 直接更新不添加新边
                in_edge.info = info

        out_node:Node = self.__nodes[jvex]

        if out_node.first_edge == None:
            out_node.first_edge = edge
        else:
            out_edge = out_node.first_edge
            while out_edge.jlink != None and out_edge.ivex != ivex:
                out_edge = out_edge.jlink
            
            if out_edge.jlink == None:
                #不存在就添加到末尾
                out_edge.jlink = edge
            else:
                #已经存在了 直接更新不添加新边
                out_edge.info = info

    

if __name__ == '__main__':

    multiple_table = Adjacency_Multiple_Table()
    multiple_table.add_node("A")
    multiple_table.add_node("B")
    multiple_table.add_node("C")
    multiple_table.add_node("D")
    multiple_table.add_node("E")

    multiple_table.add_edge(0,1,"A->B")
    multiple_table.add_edge(0,3,"A->D")
    multiple_table.add_edge(1,2,"B->C")
    multiple_table.add_edge(1,4,"B->E")
    multiple_table.add_edge(2,4,"C->E")
    multiple_table.add_edge(2,3,"C->E")
    
    
    



        