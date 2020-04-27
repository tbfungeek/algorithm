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
        if not self.is_connected_vex(vex):
            return -1
        return self.connected_vex[vex]

    def weight_of_connected_vex_by_value(self,vex_value):

        target_vex = None
        for vex in self.connected_vex.keys():
            if vex.value == vex_value:
                target_vex = vex

        if vex is None:
            return -1

        return self.connected_vex[target_vex]

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

    def vex_by_value(self,value):
        return self.vexs[value]

    def add_edge(self,start,end,weight):
        start_vex = self.add_vex(start)
        end_vex = self.add_vex(end)
        if start_vex.is_connected_vex(end):
            return
        start_vex.connect_to(end_vex,weight)
        self.edge_num += 1

    def prim(self, start_point):
        path = []

        if len(self.vexs.keys()) <= 0 or self.edge_num < self.vex_num() - 1:
            return path

        start_vex = self.vex_by_value(start_point)
        if start_vex is None:
            return path
        
        path = []
        #将起点放到已经选择的数组中
        selected_vexs = [start_vex]
        #将全部点都添加为候选点
        candidate_vexs = list(self.vexs.keys())[:]

        while len(candidate_vexs) > 0:

            begin, end, min_weight = None, None, 999999999999
            for vex in selected_vexs:
                #当前选择点的连接点
                for connected_vex in vex.connected_vexs():
                    #连接点是否与其他候选点有连接，如果没有的话则直接继续下一个循环
                    if connected_vex.value not in candidate_vexs:
                        continue
                    #有的话查看权重
                    weight = vex.weight_of_connected_vex_by_value(connected_vex.value)
                    if weight < min_weight:
                        min_weight = weight
                        begin = vex
                        end   = connected_vex
            path.append([begin, end, min_weight])
            selected_vexs.append(end)
            candidate_vexs.remove(end.value)
        return path

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

    print(g.prim(0))
    print("")
