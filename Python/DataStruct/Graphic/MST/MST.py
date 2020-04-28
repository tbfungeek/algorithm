import sys

class Vex(object):

    def __init__(self,value):
        self.value = value
        #connected_vex key 是vex结点，value是权重
        self.connected_vex = {}

    """
    和该结点连接的所有结点
    """
    def connected_vexs(self):
        return self.connected_vex.keys()

    """
    和某个结点连接边的权重
    """
    def weight_of_connected_vex_by_value(self,vex_value):

        target_vex = None
        for vex in self.connected_vex.keys():
            if vex.value == vex_value:
                target_vex = vex

        if target_vex is None:
            return -1

        return self.connected_vex[target_vex]

    """
    是否是连接的顶点
    """
    def is_connected_vex(self,vex):
        if vex not in self.connected_vexs():
            return False
        return True

    """
    添加连接顶点
    """
    def connect_to(self,vex,weight):
        if vex in self.connected_vexs():
            return
        self.connected_vex[vex] = weight

    """
    当前顶点的值
    """
    def value(self):
        return self.value

class Adjacency_Table_Graphic(object):

    def __init__(self):
        #key 对应的值  value 结点
        self.vexs = {}
        #key (start end)  value  (weight)
        self.edges = []
    
    """
    结点数
    """
    def vex_num(self):
        return len(self.vexs.keys())

    """
    边数
    """
    def edge_num(self):
        return len(self.edges)

    """
    添加结点
    """
    def add_vex(self,value):

        if value not in self.vexs.keys():
            self.vexs[value] = Vex(value)

        return self.vexs[value]

    """
    添加边
    """
    def add_edge(self,start,end,weight):
        start_vex = self.add_vex(start)
        end_vex = self.add_vex(end)
        if start_vex.is_connected_vex(end):
            return
        start_vex.connect_to(end_vex,weight)
        if start > end:
            start,end = end,start
        self.edges.append([start,end,weight]);

    """
    通过值来获取结点
    """
    def vex_by_value(self,value):
        return self.vexs[value]

    def kruskal(self):
        path = []

        if len(self.vexs.keys()) <= 0 or self.edge_num() < self.vex_num() - 1:
            return path
        
        #对边缘进行排序
        edge_list = self.edges[:]
        edge_list.sort(key=lambda a:a[2])
        
        #将结点拷贝出来
        vexs = list(self.vexs.keys())
        #将每个结点形成一个树
        trees = [[vex] for vex in vexs]

        #遍历每条边，判断边的顶点横跨了哪两个子树，如果
        for edge in edge_list:
            start_point_in_tree_index = 0
            end_point_in_tree_index = 0
            for i in range(len(trees)):
                if len(trees[i]) == 0:
                    continue
                #标记当前边的起点和终点所在的子树序号
                if edge[0] in trees[i]:
                    start_point_in_tree_index = i
                if edge[1] in trees[i]:
                    end_point_in_tree_index = i

            #如果不在一个子树上将两个不同的子树合并在一起，最终合并到只剩下一颗为止
            if start_point_in_tree_index != end_point_in_tree_index:
                trees[start_point_in_tree_index] = trees[start_point_in_tree_index] + trees[end_point_in_tree_index]
                del trees[end_point_in_tree_index]
                #只添加开始和结束两个结点在不同子树上的边，如果在同一个子树说明已经有连通路径了
                path.append(edge)

        return path

        group = [[i] for i in range(self.nodenum)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                path.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return path

    def prim(self, start_point):
        path = []
        if len(self.vexs.keys()) <= 0 or self.edge_num() < self.vex_num() - 1:
            return path

        start_vex = self.vex_by_value(start_point)
        if start_vex is None:
            return path
        
        #将起点放到已经选择的数组中
        selected_vexs = [start_vex]
        #将全部顶点值都添加为候选点
        candidate_vexs = list(self.vexs.keys())[:]
        candidate_vexs.remove(start_point)

        while len(candidate_vexs) > 0:
            begin, end, min_weight = None, None, sys.maxsize
            for selected_vex in selected_vexs:
                #获取当前选择点的连接点
                for connected_vex in selected_vex.connected_vexs():
                    #连接点是否与其他还没添加到最小生成树的候选点是否有连接。
                    if connected_vex.value not in candidate_vexs:
                        continue
                    #有的话查看连接权重
                    weight = selected_vex.weight_of_connected_vex_by_value(connected_vex.value)
                    #计算出当前选择点与所有候选点权重最小的边
                    if weight < min_weight:
                        min_weight = weight
                        begin = selected_vex
                        end   = connected_vex
            #将上一轮的最小权重边添加到path
            path.append([begin.value, end.value, min_weight])
            #将终点添加到已经访问的结点列表
            selected_vexs.append(end)
            #从候选列表中移除
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

    g.add_edge(1,0,7)
    g.add_edge(1,4,3)
    g.add_edge(1,2,9)

    g.add_edge(2,3,6)
    g.add_edge(2,1,9)
    
    g.add_edge(3,2,6)
    g.add_edge(3,4,8)
    g.add_edge(3,5,10)

    g.add_edge(4,3,8)
    g.add_edge(4,1,3)
    g.add_edge(4,5,4)

    g.add_edge(5,0,5)
    g.add_edge(5,3,10)
    g.add_edge(5,4,4)

    print(g.prim(0))

    print(g.kruskal())

    print("")
