class Vex(object):
    def __init__(self,value):
        self.value = value

class Edge(object):

    def __init__(self,start_vex_index,end_vex_index,weight):
        self.start = start_vex_index
        self.end   = end_vex_index
        self.weight = weight

class  Edge_Set(object):

    def __init__(self):
        self.vexs = []
        self.edges = []
    
    def add_edge(self,start,end,weight):
        edge = Edge(start,end,weight)
        self.edges.append(edge)
        if start not in self.vexs:
            self.vexs.append(start)
        if end not in self.vexs:
            self.vexs.append(end)

if __name__ == "__main__":
    edge_set = Edge_Set()
    edge_set.add_edge("V0","V3",5)
    edge_set.add_edge("V1","V0",4)
    edge_set.add_edge("V1","V2",3)
    edge_set.add_edge("V2","V0",8)