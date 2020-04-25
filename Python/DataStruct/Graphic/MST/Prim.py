class Vex(object):

    def __init__(self,value):
        self.value = value
        #connected_vex key 是vex结点，value是权重
        self.connected_vex = {}
    
    def connected_vexs(self):
        return self.connected_vex.keys()
    
    def weight_of_connected_vex(self,vex):
        if not self.is_connected_vex():
            return -1
        return self.connected_vex[vex]

    def is_connected_vex(self,vex):
        if vex not in self.connected_vexs():
            return False
        return True

    def connect_to(self,vex,weight):
        if vex in self.connected_vexs():
            return
        self.connected_vex[vex] = weight

    def value(self):
        return self.value

class Adjacency_Table_Graphic(object):

    def __init__(self):
        self.vexs = {}

    def add_vex(self,value):

        if value not in self.vexs.keys():
            vex = Vex(value)
            self.vexs[value] = vex

        return self.vexs[value]

    def add_edge(self,start,end,weight):
        start_vex = self.add_vex(start)
        end_vex = self.add_vex(end)
        start_vex.connect_to(end,weight)


if __name__ == "__main__":
    
    g = Adjacency_Table_Graphic()
    g.add_vex(0)
    g.add_vex(1)
    g.add_vex(2)
    g.add_vex(3)
    g.add_vex(4)
    g.add_vex(5)

    g.add_edge(0,1,7)
    g.add_edge(0,5,5)

    g.add_edge(1,0,7)
    g.add_edge(1,4,3)
    g.add_edge(1,2,9)

    g.add_edge(2,1,9)
    g.add_edge(2,3,6)

    g.add_edge(3,2,6)
    g.add_edge(3,4,8)
    g.add_edge(3,5,10)

    g.add_edge(4,3,8)
    g.add_edge(4,1,3)
    g.add_edge(4,5,4)

    g.add_edge(5,0,5)
    g.add_edge(5,3,10)
    g.add_edge(5,4,4)
