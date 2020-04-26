import math 
class Vex(object):

    def __init__(self,value):
        self.value = value
        #connected_vex key 是vex结点，value是权重
        self.connected_vex = {}
    
    def connected_vexs(self):
        return self.connected_vex.keys()

    def connected_vexs_values(self):
        return self.connected_vex.values()

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
        self.edge_num = 0
    
    def vex_num(self):
        return len(self.vexs.keys())

    def add_vex(self,value):

        if value not in self.vexs.keys():
            self.vexs[value] = Vex(value)

        return self.vexs[value]

    def add_edge(self,start,end,weight):
        start_vex = self.add_vex(start)
        end_vex = self.add_vex(end)
        if start_vex.is_connected_vex(end):
            return
        start_vex.connect_to(end,weight)
        self.edge_num += 1

    def prim(self, start_point):
        path = []
        if len(self.vexs.keys()) <= 0 or self.edge_num < self.vex_num() - 1:
            return path
        path = []
        #将起点放到已经选择的数组中
        selected_vexs = [start_point]
        #将全部点都添加为候选点
        candidate_vexs = self.vexs.keys()[:]

        while len(candidate_vexs) > 0:
            for vex in selected_vexs:
                connected_vexs = vex.connected_vex()
                for connected_vex in connected_vexs:
                    if connected_vex.value not in candidate_vexs:
                        continue
                    min_weight = 999999999999


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
    g.add_edge(1,4,3)
    g.add_edge(1,2,9)
    g.add_edge(2,3,6)
    g.add_edge(3,4,8)
    g.add_edge(3,5,10)
    g.add_edge(4,5,4)
